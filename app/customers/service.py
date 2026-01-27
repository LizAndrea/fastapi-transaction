from app.common.exceptions import NotFoundException
from app.customers.models import Customer
from app.customers.repository import CustomerRepository
from app.customers.schemas import CustomerCreate, CustomerUpdate
from app.plans.models import Plan, CustomerPlan, StatusEnum
from app.plans.repository import PlanRepository
from app.transactions.models import Transaction
from app.transactions.schemas import TransactionCreate
from app.transactions.repository import TransactionRepository

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository, plan_repository: PlanRepository, transaction_repository: TransactionRepository):
        self.customer_repository = customer_repository
        self.plan_repository = plan_repository
        self.transaction_repository = transaction_repository

    # CREATE
    def create_customer(self, customer_data: CustomerCreate) -> Customer:
        # Email uniqueness validation moved here or kept in schema?
        # Schema had it, but using DB. Ideally service does it.
        # For this step, we assume schema validation passed or we add check here.
        # But schema validation runs BEFORE service.
        # To strictly follow clean arch, schema shouldn't check DB.
        # Let's keep it simple: just create. The Unique constraint or Schema validator handles it.
        # If schema validator was removed (Refactor needed there too?), we'd check here.
        # AUDIT REPORT said: "Mover la validación de unicidad de email del Schema al Servicio"
        # So check here.
        existing = self.customer_repository.get_by_email(customer_data.email)
        if existing:
            raise ValueError("This email is already registered")

        customer = Customer.model_validate(customer_data.model_dump())
        return self.customer_repository.create(customer)

    # GET ONE
    def read_customer(self, customer_id: int) -> Customer:
        customer = self.customer_repository.get(customer_id)
        if not customer:
            raise NotFoundException(detail="Customer doesn't exist")
        return customer

    # UPDATE
    def update_customer(self, customer_id: int, customer_data: CustomerUpdate) -> Customer:
        customer = self.customer_repository.get(customer_id)
        if not customer:
            raise NotFoundException(detail="Customer doesn't exist")
        
        customer_data_dict = customer_data.model_dump(exclude_unset=True)
        customer.sqlmodel_update(customer_data_dict)
        return self.customer_repository.update(customer)

    # DELETE
    def delete_customer(self, customer_id: int):
        customer = self.customer_repository.get(customer_id)
        if not customer:
            raise NotFoundException(detail="Customer doesn't exist")
        self.customer_repository.delete(customer)
        return {"detail": "ok"}

    # GET ALL
    def get_all_customers(self):
        return self.customer_repository.get_all()

    # CREATE CUSTOMER PLAN
    def create_customer_plan(self, customer_id: int, plan_id: int, plan_status: StatusEnum):
        customer = self.customer_repository.get(customer_id)
        plan = self.plan_repository.get(plan_id)
        
        if not customer or not plan:
             raise NotFoundException(detail="Customer or Plan doesn't exist")
        
        # We need a way to create CustomerPlan. 
        # Ideally CustomerRepository handles this or PlanRepository.
        # CustomerRepository has add_plan.
        customer_plan = CustomerPlan(
            plan_id=plan.id, customer_id=customer.id, status=plan_status
        )
        return self.customer_repository.add_plan(customer_plan)

    # GET CUSTOMER PLANS
    def get_all_customer_plans(self, customer_id: int, plan_status: StatusEnum):
        customer = self.customer_repository.get(customer_id)
        if not customer:
            raise NotFoundException(detail="Customer doesn't exist")
        return self.customer_repository.get_plans(customer_id, plan_status)

    # CREATE CUSTOMER TRANSACTION
    def create_customer_transaction(self, customer_id: int, transaction_data: TransactionCreate) -> Transaction:
        customer = self.customer_repository.get(customer_id)
        if not customer:
            raise NotFoundException(detail="Customer doesn't exist")
        
        transaction_dict = transaction_data.model_dump(exclude_unset=True)
        transaction_dict["customer_id"] = customer_id
        transaction = Transaction.model_validate(transaction_dict)
        return self.transaction_repository.create(transaction)

    # GET CUSTOMER TRANSACTIONS
    def get_all_customer_transactions(self, customer_id: int):
        customer = self.customer_repository.get(customer_id)
        if not customer:
            raise NotFoundException(detail="Customer doesn't exist")
        return self.transaction_repository.get_by_customer(customer_id)

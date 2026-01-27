from sqlmodel import select, Session
from app.common.repository import BaseRepository
from app.customers.models import Customer
from app.plans.models import CustomerPlan, StatusEnum
from typing import List

class CustomerRepository(BaseRepository[Customer]):
    def __init__(self, session: Session):
        super().__init__(session, Customer)

    def get_by_email(self, email: str) -> Customer | None:
        query = select(self.model_cls).where(self.model_cls.email == email)
        return self.session.exec(query).first()
    
    def get_plans(self, customer_id: int, plan_status: StatusEnum) -> List[CustomerPlan]:
        query = (
            select(CustomerPlan)
            .where(CustomerPlan.customer_id == customer_id)
            .where(CustomerPlan.status == plan_status)
        )
        return self.session.exec(query).all()
    
    def add_plan(self, customer_plan: CustomerPlan) -> CustomerPlan:
        self.session.add(customer_plan)
        self.session.commit()
        self.session.refresh(customer_plan)
        return customer_plan

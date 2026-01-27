from typing import Annotated
from fastapi import APIRouter, Query, status, Depends, HTTPException

from app.customers.service import CustomerService
from app.customers.repository import CustomerRepository
from app.customers.models import Customer
from app.customers.schemas import CustomerCreate, CustomerUpdate
from app.plans.models import StatusEnum
from app.plans.repository import PlanRepository
from app.transactions.models import Transaction
from app.transactions.schemas import TransactionCreate
from app.transactions.repository import TransactionRepository
from app.db import SessionDep
from app.common.exceptions import NotFoundException, BadRequestException

router = APIRouter()

def get_customer_service(session: SessionDep) -> CustomerService:
    customer_repo = CustomerRepository(session)
    plan_repo = PlanRepository(session)
    transaction_repo = TransactionRepository(session)
    return CustomerService(customer_repo, plan_repo, transaction_repo)

CustomerServiceDep = Annotated[CustomerService, Depends(get_customer_service)]

# CREATE
# ----------------------
@router.post(
    "/",
    response_model=Customer,
    status_code=status.HTTP_201_CREATED,
    tags=["Customers"],
)
async def create_customer(customer_data: CustomerCreate, service: CustomerServiceDep):
    try:
        return service.create_customer(customer_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# GET ONE
# ----------------------
@router.get("/{customer_id}", response_model=Customer, tags=["Customers"])
async def read_customer(customer_id: int, service: CustomerServiceDep):
    try:
        return service.read_customer(customer_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

# UPDATE
# ----------------------
@router.patch(
    "/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED
)
async def update_customer(
    customer_id: int, customer_data: CustomerUpdate, service: CustomerServiceDep
):
    try:
        return service.update_customer(customer_id, customer_data)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

# DELETE
# ----------------------
@router.delete("/{customer_id}")
async def delete_customer(customer_id: int, service: CustomerServiceDep):
    try:
        return service.delete_customer(customer_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

# GET ALL CUSTOMERS
# ----------------------
@router.get("/", response_model=list[Customer])
async def get_all_customers(service: CustomerServiceDep):
    return service.get_all_customers()

# CREATE - CUSTOMER PLAN
# ----------------------
@router.post("/{customer_id}/plans/{plan_id}")
async def create_customer_plan(
    customer_id: int,
    plan_id: int,
    service: CustomerServiceDep,
    plan_status: StatusEnum = Query(),
):
    try:
        return service.create_customer_plan(customer_id, plan_id, plan_status)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

# List All - Customer Plans
# ----------------------
@router.get("/{customer_id}/plans")
async def get_all_customer_plans(
    customer_id: int, service: CustomerServiceDep, plan_status: StatusEnum = Query()
):
    """
    Devuelve todos los planes relacionos al usuario seleccionado,
    ademas se encuentra filtrado por su <b>estado <b/>
    """
    try:
        return service.get_all_customer_plans(customer_id, plan_status)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

# CREATE - CUSTOMER TRANSACTION
# ----------------------
@router.post("/{customer_id}/transactions", response_model=Transaction)
async def create_customer_transaction(
    customer_id: int, transaction_data: TransactionCreate, service: CustomerServiceDep
):
    """
    Crea una transacción para el usuario seleccionado.
    """
    try:
        return service.create_customer_transaction(customer_id, transaction_data)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

# GET All CUSTOMER TRANSACTIONS
# ----------------------
@router.get("/{customer_id}/transactions")
async def get_all_customer_transactions(customer_id: int, service: CustomerServiceDep):
    """
    Devuelve todas las transacciones realizadas por el usuario seleccionado
    """
    try:
        return service.get_all_customer_transactions(customer_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

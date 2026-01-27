from typing import Annotated
from fastapi import APIRouter, Query, Depends

from app.db import SessionDep
from app.transactions.service import TransactionService
from app.transactions.repository import TransactionRepository

router = APIRouter()

def get_transaction_service(session: SessionDep) -> TransactionService:
    repository = TransactionRepository(session)
    return TransactionService(repository)

TransactionServiceDep = Annotated[TransactionService, Depends(get_transaction_service)]

# GET TRANSACTIONS PAGINATE
# ----------------------
@router.get("/transaction", tags=["Transactions"])
async def get_transactions_paginate(
    service: TransactionServiceDep,
    skip: int = Query(0, description="Registros a omitir"),
    limit: int = Query(10, description="Número de registros"),
):
    return service.get_transactions_paginate(skip, limit)

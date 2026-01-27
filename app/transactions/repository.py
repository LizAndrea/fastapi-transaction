from sqlmodel import Session, select
from app.common.repository import BaseRepository
from app.transactions.models import Transaction
from typing import List

class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self, session: Session):
        super().__init__(session, Transaction)

    def get_by_customer(self, customer_id: int) -> List[Transaction]:
        query = select(self.model_cls).where(self.model_cls.customer_id == customer_id)
        return self.session.exec(query).all()

    def get_paginated(self, skip: int, limit: int) -> List[Transaction]:
        query = select(self.model_cls).offset(skip).limit(limit)
        return self.session.exec(query).all()
    
    def count(self) -> int:
        return len(self.session.exec(select(self.model_cls)).all())

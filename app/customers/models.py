from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel

from app.customers.schemas import CustomerBase
from app.plans.models import CustomerPlan

if TYPE_CHECKING:
    from app.transactions.models import Transaction
    from app.plans.models import Plan

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: List["Transaction"] = Relationship(back_populates="customer")
    plans: List["Plan"] = Relationship(
        back_populates="customers", link_model=CustomerPlan
    )
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now(), nullable=True),
    )

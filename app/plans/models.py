from enum import Enum
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, SQLModel

from app.plans.schemas import PlanBase

if TYPE_CHECKING:
    from app.customers.models import Customer

class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class CustomerPlan(SQLModel, table=True):
    __tablename__ = "customer_plan"
    id: int = Field(primary_key=True)
    plan_id: int = Field(foreign_key="plan.id")
    customer_id: int = Field(foreign_key="customer.id")
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)
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

class Plan(PlanBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
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
    customers: List["Customer"] = Relationship(
        back_populates="plans", link_model=CustomerPlan
    )

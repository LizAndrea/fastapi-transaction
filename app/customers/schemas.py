from datetime import datetime
from typing import Optional, TYPE_CHECKING
from pydantic import EmailStr, field_validator
from sqlmodel import Field, SQLModel, Session, select
from app.db import engine

if TYPE_CHECKING:
    from app.customers.models import Customer

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)

class CustomerCreate(CustomerBase):
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        from app.customers.models import Customer # Local import to avoid circular dependency
        session = Session(engine)
        query = select(Customer).where(Customer.email == value)
        result = session.exec(query).first()
        if result:
            raise ValueError("This email is already registered")
        return value

class CustomerUpdate(CustomerBase):
    pass

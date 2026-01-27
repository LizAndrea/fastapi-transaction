from sqlmodel import Field, SQLModel

class TransactionBase(SQLModel):
    ammount: int = Field(default=None)
    description: str = Field(default=None)

class TransactionCreate(TransactionBase):
    pass
    # customer_id: int = Field(foreign_key="customer.id")

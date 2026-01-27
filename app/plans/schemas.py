from sqlmodel import Field, SQLModel

class PlanBase(SQLModel):
    name: str = Field(default=None)
    price: int = Field(default=None)
    description: str | None = Field(default=None)

class PlanCreate(PlanBase):
    pass

class PlanUpdate(PlanBase):
    pass

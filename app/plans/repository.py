from sqlmodel import Session
from app.common.repository import BaseRepository
from app.plans.models import Plan

class PlanRepository(BaseRepository[Plan]):
    def __init__(self, session: Session):
        super().__init__(session, Plan)

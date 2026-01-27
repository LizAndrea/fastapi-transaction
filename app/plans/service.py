from app.common.exceptions import NotFoundException
from app.plans.models import Plan
from app.plans.schemas import PlanCreate
from app.plans.repository import PlanRepository

class PlanService:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    # GET ALL PLANS
    def get_all_plans(self):
        return self.plan_repository.get_all()
    
    # CREATE
    def create_plan(self, plan_data: PlanCreate):
        plan_db = Plan.model_validate(plan_data.model_dump())
        return self.plan_repository.create(plan_db)

    # GET ONE
    # ... (impl pending if needed)

    # UPDATE
    # ...

    # DELETE
    # ...

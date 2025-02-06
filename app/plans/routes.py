from fastapi import APIRouter, status

from app.db import SessionDep
from app.models import Plan, PlanCreate, PlanUpdate
from app.plans.service import PlanService

router = APIRouter()
service = PlanService()

# GET ALL PLANS
# ----------------------
@router.get("/", response_model=list[Plan])
async def get_all_plans(session: SessionDep):
    return service.get_all_plans(session)


# CREATE
# ----------------------
@router.post("/", response_model=Plan)
async def create_plan(plan_data: PlanCreate, session: SessionDep):
    return service.create_plan(plan_data, session)


# GET ONE
# ----------------------



# UPDATE
# ----------------------



# DELETE
# ----------------------


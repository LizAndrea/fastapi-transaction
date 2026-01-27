from typing import Annotated
from fastapi import APIRouter, status, Depends

from app.db import SessionDep
from app.plans.models import Plan
from app.plans.schemas import PlanCreate, PlanUpdate
from app.plans.service import PlanService
from app.plans.repository import PlanRepository

router = APIRouter()

def get_plan_service(session: SessionDep) -> PlanService:
    repository = PlanRepository(session)
    return PlanService(repository)

PlanServiceDep = Annotated[PlanService, Depends(get_plan_service)]

# GET ALL PLANS
# ----------------------
@router.get("/", response_model=list[Plan])
async def get_all_plans(service: PlanServiceDep):
    return service.get_all_plans()


# CREATE
# ----------------------
@router.post("/", response_model=Plan)
async def create_plan(plan_data: PlanCreate, service: PlanServiceDep):
    return service.create_plan(plan_data)


# GET ONE
# ----------------------



# UPDATE
# ----------------------



# DELETE
# ----------------------

from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.models import Plan, PlanCreate, PlanUpdate


class PlanService:

     
    # GET ALL PLANS
    # ----------------------
    def get_all_plans(self, session: SessionDep):
        return session.exec(select(Plan)).all()
    
    # CREATE
    # ----------------------
    def create_plan(self, plan_data: PlanCreate, session: SessionDep):
        plan_db = Plan.model_validate(plan_data.model_dump())
        session.add(plan_db)
        session.commit()
        session.refresh(plan_db)
        return plan_db

    # GET ONE
    # ----------------------
    

    # UPDATE
    # ----------------------



    # DELETE
    # ----------------------
    

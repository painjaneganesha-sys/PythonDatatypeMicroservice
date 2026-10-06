from fastapi import APIRouter
from pydantic import BaseModel

noneutility_router = APIRouter(prefix="/noneutility")

class NoneUtilityModel(BaseModel):
    description: str

@noneutility_router.get("/")
def get_none_utilities():
    return {"message": "None utility functions"}


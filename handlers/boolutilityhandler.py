from fastapi import APIRouter
from pydantic import BaseModel

booleanutility_router = APIRouter(prefix="/booleanutility")

class BooleanOperationModel(BaseModel):
    operation: str
    boolean_data: bool

@booleanutility_router.get("/")
async def get_boolean_methods():
    """ This returns all the methods of boolean datatype. """
    result = ["and", "or", "not"]
    return result

@booleanutility_router.post("/")
async def perform_boolean_operation(data: BooleanOperationModel):
    """ This function performs the specified boolean operation on the given boolean data. """
    operation = data.operation.lower()
    boolean_data = data.boolean_data

    if operation == "and":
        return boolean_data and True  # Example operation with True
    elif operation == "or":
        return boolean_data or False  # Example operation with False
    elif operation == "not":
        return not boolean_data
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}

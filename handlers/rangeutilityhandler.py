from fastapi import APIRouter
from pydantic import BaseModel

rangeutility_router = APIRouter(prefix="/rangeutility")

class RangeOperationModel(BaseModel):
    operation: str
    range_data: range

@rangeutility_router.get("/")
async def get_range_methods():
    """ This returns all the methods of range datatype. """
    result = ["start", "stop", "step"]
    return result

@rangeutility_router.post("/")
async def perform_range_operation(data: RangeOperationModel):
    """ This function performs the specified range operation on the given range data. """
    operation = data.operation.lower()
    range_data = data.range_data

    if operation == "start":
        return range_data.start
    elif operation == "stop":
        return range_data.stop
    elif operation == "step":
        return range_data.step
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}


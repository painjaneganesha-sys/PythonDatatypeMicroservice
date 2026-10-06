from fastapi import APIRouter
from pydantic import BaseModel

floatutility_router = APIRouter(prefix="/floatutility")


class FloatOperationModel(BaseModel):
    operation: str
    float_data: float

@floatutility_router.get("/")
async def get_float_methods():
    """ This returns all the methods of float datatype. """
    result = ["real", "imag", "conjugate"]
    return result

@floatutility_router.post("/")
async def perform_float_operation(data: FloatOperationModel):
    """ This function performs the specified float operation on the given float data. """
    operation = data.operation.lower()
    float_data = data.float_data

    if operation == "real":
        return float_data.real
    elif operation == "imag":
        return float_data.imag
    elif operation == "conjugate":
        return float_data.conjugate()
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}


from fastapi import APIRouter
from pydantic import BaseModel  

integerutility_router = APIRouter(prefix="/integerutility")

class IntegerOperationModel(BaseModel):
    operation: str
    integer_data: int

@integerutility_router.get("/")
async def get_integer_methods():
    """ This returns all the methods of integer datatype. """
    result = ["bit_length", "to_bytes", "from_bytes"]
    return result

@integerutility_router.post("/")
async def perform_integer_operation(data: IntegerOperationModel):
    """ This function performs the specified integer operation on the given integer data. """
    operation = data.operation.lower()
    integer_data = data.integer_data

    if operation == "bit_length":
        return integer_data.bit_length()
    elif operation == "to_bytes":
        return integer_data.to_bytes((integer_data.bit_length() + 7) // 8, byteorder='big')
    elif operation == "from_bytes":
        return int.from_bytes(integer_data, byteorder='big')
    else:
        return {"error": "Invalid operation specified."}    

    return {"error": "Invalid operation specified."}


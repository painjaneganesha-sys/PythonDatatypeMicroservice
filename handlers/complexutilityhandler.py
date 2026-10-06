from fastapi import APIRouter
from pydantic import BaseModel

complexity_router = APIRouter(prefix="/complexity")


class ComplexityOperationModel(BaseModel):
    operation: str
    complex_data: complex

@complexity_router.get("/")
async def get_complex_methods():
    """ This returns all the methods of complex datatype. """
    result = ["real", "imag", "conjugate"]
    return result

@complexity_router.post("/")
async def perform_complex_operation(data: ComplexityOperationModel):
    """ This function performs the specified complex operation on the given complex data. """
    operation = data.operation.lower()
    complex_data = data.complex_data

    if operation == "real":
        return complex_data.real
    elif operation == "imag":
        return complex_data.imag
    elif operation == "conjugate":
        return complex_data.conjugate()
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}    


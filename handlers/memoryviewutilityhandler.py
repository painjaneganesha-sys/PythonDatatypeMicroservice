from fastapi import APIRouter
from pydantic import BaseModel


memoryviewutility_router = APIRouter(prefix="/memoryviewutility")

class MemoryViewOperationModel(BaseModel):
    operation: str
    memoryview_data: memoryview


@memoryviewutility_router.get("/")
async def get_memoryview_methods():
    """ This returns all the methods of memoryview datatype. """
    result = ["cast", "tolist", "tobytes"]
    return result

@memoryviewutility_router.post("/")
async def perform_memoryview_operation(data: MemoryViewOperationModel):
    """ This function performs the specified memoryview operation on the given memoryview data. """
    operation = data.operation.lower()
    memoryview_data = data.memoryview_data

    if operation == "cast":
        return memoryview_data.cast("B")  # Example cast to bytes
    elif operation == "tolist":
        return memoryview_data.tolist()
    elif operation == "tobytes":
        return memoryview_data.tobytes()
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}


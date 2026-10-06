from fastapi import APIRouter
from pydantic import BaseModel

tuple_utility_router = APIRouter(prefix="/tupleutility")

class TupleOperationModel(BaseModel):
    operation: str
    tuple_data: tuple

@tuple_utility_router.get("/")
async def get_tuple_methods():
    """ This returns all the methods of tuple datatype. """
    result = ["count", "index"]
    return result

@tuple_utility_router.post("/")
async def perform_tuple_operation(data: TupleOperationModel):
    """ This function performs the specified tuple operation on the given tuple data. """
    operation = data.operation.lower()
    tuple_data = data.tuple_data

    if operation == "count":
        return tuple_data.count("element_to_count")  # Example element
    elif operation == "index":
        return tuple_data.index("element_to_find") if "element_to_find" in tuple_data else None
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}


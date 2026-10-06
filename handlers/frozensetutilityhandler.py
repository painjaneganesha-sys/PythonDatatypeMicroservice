from fastapi import APIRouter
from pydantic import BaseModel

frozensetutility_router = APIRouter(prefix="/frozensetutility")

class FrozensetOperationModel(BaseModel):
    operation: str
    frozenset_data: frozenset

@frozensetutility_router.get("/")
async def get_frozenset_methods():
    """ This returns all the methods of frozenset datatype. """
    result = ["copy", "difference", "intersection", "isdisjoint", "issubset", "issuperset", "union"]
    return result

@frozensetutility_router.post("/")
async def perform_frozenset_operation(data: FrozensetOperationModel):
    """ This function performs the specified frozenset operation on the given frozenset data. """
    operation = data.operation.lower()
    frozenset_data = data.frozenset_data

    if operation == "copy":
        return frozenset_data.copy()
    elif operation == "difference":
        return frozenset_data.difference({"element1", "element2"})  # Example elements
    elif operation == "intersection":
        return frozenset_data.intersection({"element1", "element2"})  # Example elements
    elif operation == "isdisjoint":
        return frozenset_data.isdisjoint({"element1", "element2"})  # Example elements
    elif operation == "issubset":
        return frozenset_data.issubset({"element1", "element2"})  # Example elements
    elif operation == "issuperset":
        return frozenset_data.issuperset({"element1", "element2"})  # Example elements
    elif operation == "union":
        return frozenset_data.union({"element1", "element2"})  # Example elements
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}

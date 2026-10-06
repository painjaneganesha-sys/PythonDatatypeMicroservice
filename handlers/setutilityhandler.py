from fastapi import APIRouter
from pydantic import BaseModel  


setutility_router = APIRouter(prefix="/setutility")

class SetOperationModel(BaseModel):
    operation: str
    set_data: set   

@setutility_router.get("/")
async def get_set_methods():
    """ This returns all the methods of set datatype. """
    result = ["add", "clear", "copy", "difference", "difference_update", 
              "discard", "intersection", "intersection_update", 
              "isdisjoint", "issubset", "issuperset", "pop", 
              "remove", "symmetric_difference", 
              "symmetric_difference_update", "union", "update"]
    return result   


@setutility_router.post("/")
async def perform_set_operation(data: SetOperationModel):
    """ This function performs the specified set operation on the given set data. """
    operation = data.operation.lower()
    set_data = data.set_data

    if operation == "add":
        set_data.add("new_element")  # Example element to add
        return set_data
    elif operation == "clear":
        set_data.clear()
        return set_data
    elif operation == "copy":
        return set_data.copy()
    elif operation == "difference":
        return set_data.difference({"element1", "element2"})  # Example elements
    elif operation == "difference_update":
        set_data.difference_update({"element1", "element2"})  # Example elements
        return set_data
    elif operation == "discard":
        set_data.discard("element_to_discard")  # Example element to discard
        return set_data
    elif operation == "intersection":
        return set_data.intersection({"element1", "element2"})  # Example elements
    elif operation == "intersection_update":
        set_data.intersection_update({"element1", "element2"})  # Example elements
        return set_data
    elif operation == "isdisjoint":
        return set_data.isdisjoint({"element1", "element2"})  # Example elements
    elif operation == "issubset":
        return set_data.issubset({"element1", "element2"})  # Example elements
    elif operation == "issuperset":
        return set_data.issuperset({"element1", "element2"})  # Example elements
    elif operation == "pop":
        return set_data.pop() if set_data else None
    elif operation == "remove":
        try:
            set_data.remove("element_to_remove")  # Example element to remove
            return set_data
        except KeyError:
            return {"error": "Element not found in the set."}
    elif operation == "symmetric_difference":
        return set_data.symmetric_difference({"element1", "element2"})  # Example elements
    elif operation == "symmetric_difference_update":
        set_data.symmetric_difference_update({"element1", "element2"})  # Example elements
        return set_data
    elif operation == "union":
        return set_data.union({"element1", "element2"})  # Example elements
    elif operation == "update":
        set_data.update({"new_element1", "new_element2 "})  # Example elements to add
        return set_data
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}


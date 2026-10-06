from fastapi import APIRouter
from pydantic import BaseModel  

listutility_router = APIRouter(prefix="/listutility")

class ListOperationModel(BaseModel):
    operation: str
    list_data: list

@listutility_router.get("/")
async def get_list_methods():
    """ This returns all the methods of list datatype. """
    result = ["append", "clear", "copy", "count", "extend", "index", 
              "insert", "pop", "remove", "reverse", "sort"]
    return result

@listutility_router.post("/")
async def perform_list_operation(data: ListOperationModel):
    """ This function performs the specified list operation on the given list data. """
    operation = data.operation.lower()
    list_data = data.list_data

    if operation == "append":
        list_data.append("new_element")  # Example element to append
        return list_data
    elif operation == "clear":
        list_data.clear()
        return list_data
    elif operation == "copy":
        return list_data.copy()
    elif operation == "count":
        return list_data.count("element_to_count")  # Example element
    elif operation == "extend":
        list_data.extend(["new_element1", "new_element2"])  # Example elements to extend
        return list_data
    elif operation == "index":
        return list_data.index("element_to_find") if "element_to_find" in list_data else None
    elif operation == "insert":
        list_data.insert(0, "new_element")  # Example element to insert
        return list_data
    elif operation == "pop":
        return list_data.pop() if list_data else None
    elif operation == "remove":
        try:
            list_data.remove("element_to_remove")  # Example element to remove
            return list_data
        except ValueError:
            return {"error": "Element not found in the list."}
    elif operation == "reverse":
        list_data.reverse()
        return list_data
    elif operation == "sort":
        list_data.sort()
        return list_data
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}


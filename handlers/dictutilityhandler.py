from fastapi import APIRouter
from pydantic import BaseModel

dictutility_router = APIRouter(prefix="/dictutility")

class DictOperationModel(BaseModel):
    operation: str
    dict_data: dict


@dictutility_router.get("/")
async def get_dict_methods():
    """ This returns all the methods of dict datatype. """
    result = ["clear", "copy", "fromkeys", "get", "items", "keys", 
              "pop", "popitem", "setdefault", "update", "values"]
    return result


@dictutility_router.post("/")
async def perform_dict_operation(data: DictOperationModel):
    """ This function performs the specified dict operation on the given dict data. """
    operation = data.operation.lower()
    dict_data = data.dict_data

    if operation == "clear":
        dict_data.clear()
        return dict_data
    elif operation == "copy":
        return dict_data.copy()
    elif operation == "fromkeys":
        return dict.fromkeys(["key1", "key2"], "default_value")  # Example keys and default value
    elif operation == "get":
        return dict_data.get("key_to_get", "default_value")  # Example key and default value
    elif operation == "items":
        return list(dict_data.items())
    elif operation == "keys":
        return list(dict_data.keys())
    elif operation == "pop":
        return dict_data.pop("key_to_pop", "default_value")  # Example key and default value
    elif operation == "popitem":
        return dict_data.popitem() if dict_data else None
    elif operation == "setdefault":
        return dict_data.setdefault("key_to_set", "default_value")  # Example key and default value
    elif operation == "update":
        dict_data.update({"new_key": "new_value"})  # Example key-value pair to update
        return dict_data
    elif operation == "values":
        return list(dict_data.values())
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}

    

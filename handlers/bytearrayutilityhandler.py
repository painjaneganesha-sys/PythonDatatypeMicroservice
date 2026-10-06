from fastapi import APIRouter
from pydantic import BaseModel

bytearrayutility_router = APIRouter(prefix="/bytearrayutility")


class ByteArrayOperationModel(BaseModel):
    operation: str
    bytearray_data: bytearray


@bytearrayutility_router.get("/")
async def get_bytearray_methods():
    """ This returns all the methods of bytearray datatype. """
    result = ["append", "extend", "insert", "remove", "pop", "clear", "index", "count", "reverse"]
    return result

@bytearrayutility_router.post("/")
async def perform_bytearray_operation(data: ByteArrayOperationModel):
    """ This function performs the specified bytearray operation on the given bytearray data. """
    operation = data.operation.lower()
    bytearray_data = data.bytearray_data

    if operation == "append":
        bytearray_data.append(65)  # Example: Append ASCII value of 'A'
        return bytearray_data
    elif operation == "extend":
        bytearray_data.extend(b"BC")  # Example: Extend with bytes for 'B' and 'C'
        return bytearray_data
    elif operation == "insert":
        bytearray_data.insert(1, 66)  # Example: Insert ASCII value of 'B' at index 1
        return bytearray_data
    elif operation == "remove":
        try:
            bytearray_data.remove(65)  # Example: Remove ASCII value of 'A'
            return bytearray_data
        except ValueError:
            return {"error": "Element not found in the bytearray."}
    elif operation == "pop":
        return bytearray_data.pop() if bytearray_data else None
    elif operation == "clear":
        bytearray_data.clear()
        return bytearray_data
    elif operation == "index":
        try:
            return bytearray_data.index(66)  # Example: Find index of ASCII value of 'B'
        except ValueError:
            return {"error": "Element not found in the bytearray."}
    elif operation == "count":
        return bytearray_data.count(66)  # Example: Count occurrences of ASCII value of 'B'
    elif operation == "reverse":
        bytearray_data.reverse()
        return bytearray_data
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}    


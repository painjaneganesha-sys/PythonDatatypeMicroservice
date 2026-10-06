from fastapi import APIRouter
from pydantic import BaseModel

bytesutility_router = APIRouter(prefix="/bytesutility")


class BytesOperationModel(BaseModel):
    operation: str
    bytes_data: bytes


@bytesutility_router.get("/")
async def get_bytes_methods():
    """ This returns all the methods of bytes datatype. """
    result = ["capitalize", "center", "count", "decode", "endswith", "find", "hex", "index", "isalnum", "isalpha",
              "isdigit", "islower", "isspace", "istitle", "isupper", "join", "ljust", "lower", "lstrip",
              "partition", "replace", "rfind", "rindex", "rjust", "rstrip", "split", "splitlines",
              "startswith", "strip", "swapcase", "title", "upper"]
    return result

@bytesutility_router.post("/")
async def perform_bytes_operation(data: BytesOperationModel):
    """ This function performs the specified bytes operation on the given bytes data. """
    operation = data.operation.lower()
    bytes_data = data.bytes_data

    if operation == "capitalize":
        return bytes_data.capitalize()
    elif operation == "center":
        return bytes_data.center(20)  # Example width
    elif operation == "count":
        return bytes_data.count(b"a")  # Example substring
    elif operation == "decode":
        return bytes_data.decode()
    elif operation == "endswith":
        return bytes_data.endswith(b"a")  # Example suffix
    elif operation == "find":
        return bytes_data.find(b"a")  # Example substring
    elif operation == "hex":
        return bytes_data.hex()
    elif operation == "index":
        try:
            return bytes_data.index(b"a")  # Example substring
        except ValueError:
            return -1
    elif operation == "isalnum":
        return bytes_data.isalnum()
    elif operation == "isalpha":
        return bytes_data.isalpha()
    elif operation == "isdigit":
        return bytes_data.isdigit()
    elif operation == "islower":
        return bytes_data.islower()
    elif operation == "isspace":
        return bytes_data.isspace()
    elif operation == "istitle":
        return bytes_data.istitle()
    elif operation == "isupper":
        return bytes_data.isupper()
    elif operation == "join":
        return b",".join([bytes_data, b"example"])  # Example join
    elif operation == "ljust":
        return bytes_data.ljust(20)  # Example width
    elif operation == "lower":
        return bytes_data.lower()
    elif operation == "lstrip":
        return bytes_data.lstrip()
    elif operation == "partition":
        return bytes_data.partition(b"a")  # Example separator
    elif operation == "replace":
        return bytes_data.replace(b"a", b"b")  # Example replacement
    elif operation == "rfind":          
        return bytes_data.rfind(b"a")  # Example substring
    elif operation == "rindex":
        try:
            return bytes_data.rindex(b"a")  # Example substring
        except ValueError:
            return -1
    elif operation == "rjust":
        return bytes_data.rjust(20)  # Example width
    elif operation == "rstrip":
        return bytes_data.rstrip()
    elif operation == "split":  
        return bytes_data.split()  # Example split by whitespace
    elif operation == "splitlines":
        return bytes_data.splitlines()  # Example split by lines
    elif operation == "startswith":
        return bytes_data.startswith(b"a")  # Example prefix
    elif operation == "strip":
        return bytes_data.strip()
    elif operation == "swapcase":
        return bytes_data.swapcase()
    elif operation == "title":
        return bytes_data.title()
    elif operation == "upper":
        return bytes_data.upper()
    else:
        return {"error": "Invalid operation specified."}    

    return {"error": "Invalid operation specified."}


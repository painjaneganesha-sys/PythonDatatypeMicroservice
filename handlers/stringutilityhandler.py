from fastapi import APIRouter
from pydantic import BaseModel

stringutility_router = APIRouter(prefix="/stringutility")

class StringOperationModel(BaseModel):
    operation: str
    text: str

@stringutility_router.get("/")
async def get_string_methods():
    """ This returns all the methods of string datatype. """
    result = ["capitalize", "casefold", "center", "count", "encode", "endswith", 
              "expandtabs", "find", "format", "format_map", "index", "isalnum", 
              "isalpha", "isascii", "isdecimal", "isdigit", "isidentifier", 
              "islower", "isnumeric", "isprintable", "isspace", "istitle", 
              "isupper", "join", "ljust", "lower", "lstrip", "partition", 
              "replace", "rfind", "rindex", "rjust", "rstrip", "split", 
              "splitlines", "startswith", "strip", "swapcase", 
              "title", "upper"]
    return result   

async def perform_string_operation(data: StringOperationModel):
    """ This function performs the specified string operation on the given text. """
    operation = data.operation.lower()
    text = data.text

    if operation == "capitalize":
        return text.capitalize()
    elif operation == "casefold":
        return text.casefold()
    elif operation == "center":
        return text.center(20)  # Example width
    elif operation == "count":
        return text.count("a")  # Example substring
    elif operation == "encode":
        return text.encode()
    elif operation == "endswith":
        return text.endswith("a")  # Example suffix
    elif operation == "expandtabs":
        return text.expandtabs(4)  # Example tab size
    elif operation == "find":
        return text.find("a")  # Example substring
    elif operation == "format":
        return "{}".format(text)
    elif operation == "format_map":
        return "{text}".format_map({"text": text})
    elif operation == "index":
        try:
            return text.index("a")  # Example substring
        except ValueError:
            return -1
    elif operation == "isalnum":
        return text.isalnum()
    elif operation == "isalpha":
        return text.isalpha()
    elif operation == "isascii":
        return text.isascii()
    elif operation == "isdecimal":
        return text.isdecimal()
    elif operation == "isdigit":
        return text.isdigit()
    elif operation == "isidentifier":
        return text.isidentifier()
    elif operation == "islower":
        return text.islower()
    elif operation == "isnumeric":
        return text.isnumeric()
    elif operation == "isprintable":
        return text.isprintable()
    elif operation == "isspace":
        return text.isspace()
    elif operation == "istitle":
        return text.istitle()
    elif operation == "isupper":
        return text.isupper()
    elif operation == "join":
        return "-".join(text)  # Example separator
    elif operation == "ljust":
        return text.ljust(20)  # Example width
    elif operation == "lower":      
        return text.lower()
    elif operation == "lstrip":
        return text.lstrip()
    elif operation == "partition":
        return text.partition("a")  # Example separator
    elif operation == "replace":    
        return text.replace("a", "b")  # Example replacement
    elif operation == "rfind":
        return text.rfind("a")  # Example substring
    elif operation == "rindex":
        try:
            return text.rindex("a")  # Example substring
        except ValueError:
            return -1
    elif operation == "rjust":
        return text.rjust(20)  # Example width
    elif operation == "rstrip":
        return text.rstrip()
    elif operation == "split":      
        return text.split()  # Example split by whitespace
    elif operation == "splitlines":
        return text.splitlines()
    elif operation == "startswith":
        return text.startswith("a")  # Example prefix
    elif operation == "strip":
        return text.strip()
    elif operation == "swapcase":
        return text.swapcase()
    elif operation == "title":
        return text.title()
    elif operation == "upper":
        return text.upper()
    else:
        return "Invalid operation"  

    return "Invalid operation"


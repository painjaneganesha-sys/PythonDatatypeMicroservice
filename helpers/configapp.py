from fastapi import FastAPI
from handlers.listutilityhandler import listutility_router
from handlers.dictutilityhandler import dictutility_router
from handlers.setutilityhandler import setutility_router
from handlers.tupleutilityhandler import tuple_utility_router   
from handlers.integerutilityhandler import integerutility_router
from handlers.stringutilityhandler import stringutility_router
from handlers.floatutilityhandler import floatutility_router
from handlers.boolutilityhandler import booleanutility_router
# from handlers.complexutilityhandler import complexutility_router
# from handlers.bytesutilityhandler import bytesutility_router
# from handlers.bytearrayutilityhandler import bytearrayutility_router
# from handlers.memoryviewutilityhandler import memoryviewutility_router
from handlers.frozensetutilityhandler import frozensetutility_router
# from handlers.rangeutilityhandler import rangeutility_router
from handlers.noneutilityhandler import noneutility_router

all_router = [
    listutility_router,
    dictutility_router,
    setutility_router,
    tuple_utility_router,
    integerutility_router,
    stringutility_router,
    floatutility_router,
    booleanutility_router,
    # complexutility_router,
    # bytesutility_router,
    # bytearrayutility_router,
    # memoryviewutility_router,
    frozensetutility_router,
    # rangeutility_router,
    noneutility_router
]

def config_app() :
    app = FastAPI(title = "Datatypes in python and it's methods ")
    for router in all_router :
        app.include_router(router)
    return app

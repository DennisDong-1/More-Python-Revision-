import logging 
import time 
from datetime import datetime 
logger = logging.getLogger("Database Logger")
logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
logger.setLevel(logging.INFO)

def LoggingFunction(func): 
    def wrapper_function(*args, **kwargs): 
        start = time.time() 
        # Calling the function 
        result = func(*args, **kwargs)
        stop = time.time() 
        logger.info(f" the {func.__name__} took {stop-start:4f} seconds")
        return result 
    
    return wrapper_function

@LoggingFunction
def a_database_connection(): 
    print("Fetching data from database")
    time.sleep(3) # Simulating the database fetech operation 
    print("Sucessfully fetched data from database") 
    return {"status": "400"}

print(a_database_connection())
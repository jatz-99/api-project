from unittest import result

from fastapi import FastAPI  

app = FastAPI()
@app.get("/fa/{no}")
def fa (no:int):
    result=1
    for i in range(1, no+1):
        result = result * i
    return result

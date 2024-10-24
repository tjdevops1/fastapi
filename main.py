from fastapi import FastAPI

app = FastAPI()

# Route to get basic info
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI on EKS!"}

# Route to perform addition
@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

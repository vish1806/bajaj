from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class RequestData(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def process_data(request: RequestData):
    numbers = [item for item in request.data if item.isdigit()]
    alphabets = [item for item in request.data if item.isalpha()]
    highest_lowercase_alphabet = [ch for ch in sorted(set(filter(str.islower, alphabets))) if ch == sorted(filter(str.islower, alphabets))[-1]]
    
    return {
        "is_success": True,
        "user_id": "Vishal",
        "email": "vishal.ganapathy2021@vitstudent.ac.in",
        "roll_number": "21BCE0751",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

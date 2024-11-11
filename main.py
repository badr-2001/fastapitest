from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: str
    name: str
    Age: str 
    Sexe: float | None = None

users = []

@app.get("/")
def hello(): 
    return {"message": "Hello this is our API !!"}

@app.post("/addUser")
def addUser(user: User): 
    users.append(user)
    return {"message": "User Successfully Added!"}

@app.get("/getUsers")
def getUsers(): 
    return {"users": [user.dict() for user in users]}

@app.delete("/deleteUser/{index}")
def deleteUser(index: int): 
    # Check if the index is valid (within the range of the list)
    if index < 0 or index >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    
    # Remove the user by index
    deleted_user = users.pop(index)
    
    return {"message": f"User {deleted_user.name} has been deleted successfully"}

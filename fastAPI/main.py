from fastapi import FastAPI, HTTPException
from models import User,Gender,Role
from typing import List
from uuid import UUID, uuid4

app=FastAPI()
db: List[User] = [ User(id=uuid4(),
                        first_name="A",
                        last_name="B",
                        gender=Gender.female,
                        roles=[Role.student] ),
                   User(id=uuid4(),
                        first_name="C",
                        last_name="D",
                        gender=Gender.male,
                        roles=[Role.admin, Role.user] )
                ]

@app.get("/")
def root():
    return {"Hello":"World1"}

@app.get("/api/v1/users")
def fetch_user():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"{user_id} not present"
    )

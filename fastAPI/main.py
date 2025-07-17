from fastapi import FastAPI
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

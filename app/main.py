from fastapi import FastAPI
# import user from routers 
from routers.user import User


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/users/")
async def create_user(user: User):


    return user


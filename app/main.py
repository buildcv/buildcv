from fastapi import FastAPI
# import user from routers 
from schemas.user import UserBase
from utils.crud import get_all_users , create_user
from schemas.user import UserBase
app = FastAPI()



@app.get("/users/",response_model=list[UserBase])
async def get_users():

    return get_all_users()



@app.post("/users/",response_model=UserBase)
def create_new_user(user: UserBase):
    print(user)

    create_user(user)

    return user


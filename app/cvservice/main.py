from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import user from routers 
from schemas.user import UserBase
from schemas.education import Education as EducationSchema 

from utils.crud import create_education_entry, get_all_users , create_user
from schemas.user import UserBase
app = FastAPI()

app.mount("/static/", StaticFiles(directory="static"), name="static")






@app.get("/users/",response_model=list[UserBase])
async def get_users():

    return get_all_users()



@app.post("/users/",response_model=UserBase  )
async def create_new_user(user: UserBase):
    print(user)

    create_user(user)

    return user




@app.post("/education")
async def dashboard(education: EducationSchema):
    print(education)

    created_education = create_education_entry(education)

    return created_education
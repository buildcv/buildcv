from cgitb import html
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import user from routers 
from schemas.user import UserBase
from schemas.education import (
    Education_description, Education_end_date,
     Education_school, Education_start_date,
      EducationDel, EducationSchema
)
from unit_tests.education_update_test import update_education_end_date 

from utils.crud import  get_all_users , create_user
from utils.crud_education import (
    delete_education, delete_education_degree, delete_education_description,
     delete_education_end_date, delete_education_school_name, 
     delete_education_start_date, update_education_school_name ,
      update_education_description 
    , update_education_start_date 
)
from schemas.user import UserBase
app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")






@app.get("/users/",response_model=list[UserBase])
async def get_users():

    return get_all_users()



@app.post("/users/",response_model=UserBase , status_code=201 )
async def create_new_user(user: UserBase):
    print(user)

    create_user(user)

    return user




# update education entry
@app.put("/education")
async def dashboard(education: EducationSchema):
    print(education)

    

    pass 


@app.put("/education/school")
async def update_edu_school(school : Education_school):
    print(school)
    update_education_school_name(school.cv_id , school.school)


    return {"status": "success" , "status_code": 200}



@app.put("/education/description")
async def update_edu_description(description : Education_description):
    print(description)
    update_education_description(description.cv_id , description.description)


    return {"status": "success" , "status_code": 200}
    

@app.put("/education/start-date")
async def update_edu_start_date(start_date : Education_start_date):
    print(start_date)
    update_education_start_date(start_date.cv_id , start_date.start_date)


    return {"status": "success" , "status_code": 200}    


@app.put("/education/end-date")
async def update_edu_end_date(end_date : Education_end_date):
    print(end_date)
    update_education_end_date(end_date.cv_id , end_date.end_date)


    return {"status": "success" , "status_code": 200}

# delete education school name 
@app.delete("/education/school")
async def delete_edu_school(delete_id : EducationDel):
    print(delete_id)
    delete_education_school_name(delete_id.cv_id)


    return {"status": "success" , "status_code": 200}

# delete education degree 
@app.delete("/education/degree")
async def delete_edu_degree(delete_id : EducationDel):
    print(delete_id)
    delete_education_degree(delete_id.cv_id)


    return {"status": "success" , "status_code": 200}


# delete education description
@app.delete("/education/description")
async def delete_edu_description(delete_id : EducationDel):
    print(delete_id)
    delete_education_description(delete_id.cv_id)


    return {"status": "success" , "status_code": 200}

# delete education start date
@app.delete("/education/start-date")
async def delete_edu_start_date(delete_id : EducationDel):
    print(delete_id)
    delete_education_start_date(delete_id.cv_id)


    return {"status": "success" , "status_code": 200}

# delete education end date
@app.delete("/education/end-date")
async def delete_edu_end_date(delete_id : EducationDel):
    print(delete_id)
    delete_education_end_date(delete_id.cv_id)


    return {"status": "success" , "status_code": 200}

# delete education entry
@app.delete("/education")
async def delete_edu_entry(delete_id : EducationDel):
    print(delete_id)
    delete_education(delete_id.cv_id)


    return {"status": "success" , "status_code": 200}
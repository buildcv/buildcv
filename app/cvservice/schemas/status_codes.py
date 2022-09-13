from pydantic import BaseModel


class Response_base_200(BaseModel):
    status_code: int


class Response_user_created_201(BaseModel):
    status_code: int = 201
    status: str = "user created"

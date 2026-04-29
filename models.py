from pydantic import BaseModel

class UserInfo(BaseModel):
    username: str
    password: str
    roles: list[str]

class UserLogin(BaseModel):
    username: str
    password: str

class message(BaseModel):
    username: str
    msg: str
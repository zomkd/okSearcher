from pydantic import BaseModel


class Credentials(BaseModel):
    username: str = ""
    password: str = ""
    application_id: str = ""
    application_key: str = ""
    application_secret_key: str = ""
    session_key: str = ""
    session_secret_key: str = ""


class SearchParams(BaseModel):
    firstname: str = ""
    secondname: str = ""
    fromAge: str = ""
    tillAge: str = ""
    city: str = ""
    country: str = ""

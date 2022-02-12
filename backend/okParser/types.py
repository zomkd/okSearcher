from pydantic import BaseModel


class Credentials(BaseModel):
    username: str = ""
    password: str = ""
    application_id: str = ""
    application_key: str = ""
    application_secret_key: str = ""
    session_key: str = ""
    session_secret_key: str = ""

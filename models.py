from typing import List, Optional

from pydantic import BaseModel

class EmailBody(BaseModel):
    subject: str = "E-mail de teste!"
    message: str = "Mensagem de teste!"
    destinatario: List[str] = ["sanchobuendia@gmail.com"]
    email_user: str = "aureliano@outlook.com"
    secret_key: str
from fastapi import FastAPI
import api_send

app = FastAPI()

app.include_router(api_send.router, tags=["sendemail"], prefix="/api")
app.include_router(api_send.router, tags=["hello"],     prefix="/api")


from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import os
import pandas as pd
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from models import EmailBody

general_log = logging.getLogger('general_log')
general_log.propagate = False

router = APIRouter()

@router.get("/hello", operation_id="hello")
def HeloWorld():
    return "Hello World!"

@router.post("/sendemail", operation_id="sendemail", 
           status_code=200,
           responses= { 200: {'description': 'Email sent!'},
                        400: {'description': 'Invalid request body.'}
                       }
                       )

def email(body: EmailBody):   
    try:
        email_port = 587
        email_host = "smtp.office365.com"
        
        for i in body.destinatario:
            general_log.info('E-mail_alert: starting server object.') 
            server = smtplib.SMTP(email_host, email_port)

            general_log.info('E-mail_alert: logging on')
            server.ehlo()
            server.starttls()
            server.login(body.email_user, body.secret_key)

            email_msg = MIMEMultipart()
            email_msg['From'] = body.email_user
            email_msg['To'] = i
            email_msg['Subject'] = body.subject
            general_log.info('E-mail_alert: attaching the message')
            email_msg.attach(MIMEText(body.message, 'html'))

            general_log.info(f"E-mail_alert: sending the message to: {i}")
            server.sendmail(body.email_user, body.destinatario, email_msg.as_string())
            general_log.info('E-mail_alert: message sent!')
            server.quit()

        return JSONResponse(content={"message": "Email sent!"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

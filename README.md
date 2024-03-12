# Sending Email with Attachment using Python Script

This Python script allows you to send an email with an attachment using a specified endpoint URL.

## Prerequisites

Before using the script, make sure you have the following:

1. Python installed on your system.
2. Necessary libraries installed:
    - `google-auth`
    - `requests`

## Setup

1. Replace the placeholder values in the script with your actual credentials and data:
    - `SERVICE_FILENAME`: Filename of the service account credentials file.
    - `AUDIENCE`: Audience for the service account.
    - `url`: Endpoint URL for sending the email.
    - `data_to_send`: Dictionary containing email details like sender, recipient, message, and subject.
    - Ensure you have the file `"file_name.csv"` in the same directory as the script or provide the correct file path.

## Usage

The script will send the email with the specified attachment.

uvicorn main:app --reload

## Troubleshooting

If you encounter any issues while using the script, ensure:

- Your service account credentials file (`SERVICE_FILENAME`) is correctly specified.
- The target audience (`AUDIENCE`) is accurate.
- The endpoint URL (`url`) is accessible and correctly configured.
- The file you're attaching exists and is accessible by the script.

## Python Script (`send_email_with_attachment.py`)

```python
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

SERVICE_FILENAME = 'apisendemail.json'
AUDIENCE = '226884483962-hua4aeuoq65uacmgeimonrekho5hld28.apps.googleusercontent.com'

url = 'https://apiemail-dot-ped-dev-308120.rj.r.appspot.com/api/sendemail' 
data = {
    "email_user":"aureliano.paiva@grupofleury.com.br",
    "destinatario": ["sanchobuendia@gmail.com", "aureliano.paiva@grupofleury.com.br"],
    "message": "Teste GCP",
    "subject": "Subject Appengine",
    "secret_key": "dabsa5-fesnob-Qupqyc"
}

credentials = service_account.IDTokenCredentials.from_service_account_file(SERVICE_FILENAME, target_audience=AUDIENCE)

session = AuthorizedSession(credentials)

r = session.post(url, json = data)
```


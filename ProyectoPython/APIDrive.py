# pip install google-api-python-client
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = "12PsIRUZsjQmH6sGYL0ueoigy1NcyRJzl"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_name = os.path.basename(file_path)  # Obtiene el nombre del archivo local

    file_metadata = {
        'name': file_name,  # Establece el nombre del archivo en el nombre del archivo local
        'parents': [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()




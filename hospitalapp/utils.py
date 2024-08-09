# utils.py

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as GoogleCredentials
from .models import DoctorOAuthToken

def refresh_credentials(doctor):
    token_record = DoctorOAuthToken.objects.get(doctor=doctor)
    credentials = GoogleCredentials(
        token=token_record.access_token,
        refresh_token=token_record.refresh_token,
        token_uri='https://oauth2.googleapis.com/token',
        client_id='YOUR_CLIENT_ID',  # Replace with your actual client ID
        client_secret='YOUR_CLIENT_SECRET',  # Replace with your actual client secret
    )

    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
        # Update the database with the new credentials
        token_record.access_token = credentials.token
        token_record.refresh_token = credentials.refresh_token
        token_record.token_expiry = credentials.expiry
        token_record.save()

    return credentials

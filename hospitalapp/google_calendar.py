from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
from datetime import datetime

# Define the scopes you need
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_credentials():
    """Fetch or refresh OAuth 2.0 credentials."""
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def create_calendar_event(email, summary, description, date, start_time, end_time):
    # Load credentials from a file or session
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)

    # Combine date and start_time to create datetime objects
    start_datetime = datetime.strptime(f"{date} {start_time}", '%Y-%m-%d %H:%M')
    end_datetime = datetime.strptime(f"{date} {end_time}", '%Y-%m-%d %H:%M')

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [
            {'email': email},
        ],
    }

    try:
        # Insert the event into the calendar
        created_event = service.events().insert(calendarId='primary', body=event).execute()
        return created_event
    except Exception as e:
        # Handle errors (e.g., API errors)
        print(f"An error occurred: {e}")
        return None

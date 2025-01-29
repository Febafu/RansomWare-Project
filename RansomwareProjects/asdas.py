import os.path
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Authenticate and build service
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

# Create the email message
message = MIMEMultipart()
message['to'] = "bahaduribadov2@gmail.com"
message['subject'] = "Test Email from Python"
msg = MIMEText("This is a test message")
message.attach(msg)

raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

# Send the email
send_message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
print('Message sent successfully: %s' % send_message['id'])

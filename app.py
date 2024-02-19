import os
import pickle
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
TOKEN_PICKLE_FILE = 'token.pickle'
CREDENTIALS_FILE = 'credentials.json'

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_message(html, to_email, from_email, subject):
    message = MIMEText(html, "html")
    message['to'] = to_email
    message['from'] = from_email
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f'Message Id: {message["id"]}')
    except HttpError as error:
        print(f'Um erro ocorreu ao enviar a mensagem: {error}')

def main():
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    html = """
        <html>
        <head>
            <style>p { color: red; }</style>
        </head>
        <body><p>Olá, Mundo!</p></body>
        </html>
        """

    message = create_message(html, "teste@teste.com", "teste@teste.com", "Assunto do e-mail")
    send_message(service, "me", message)
    print("E-mail enviado com sucesso!")

if __name__ == '__main__':
    main()

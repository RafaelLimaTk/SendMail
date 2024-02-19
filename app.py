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

def main():
    creds = None
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('gmail', 'v1', credentials=creds)

        html = """
            <html>
            <head>
                <style>
                p { color: red; }
                </style>
            </head>
            <body>
                <p>Olá, Mundo!</p>
            </body>
            </html>
            """

        message = MIMEText(html, "html")
        message['to'] = "rafamano123.rl@gmail.com"
        message['from'] = "cursogti19@gmail.com"
        message['subject'] = "Assunto do e-mail"

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        send_message(service, "me", {'raw': encoded_message})
        print("E-mail enviado com sucesso!")
    except HttpError as error:
        print(f'Um erro ocorreu: {error}')

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f'Message Id: {message["id"]}')
        return message
    except HttpError as error:
        print(f'Um erro ocorreu ao enviar a mensagem: {error}')
        return None

if __name__ == '__main__':
    main()

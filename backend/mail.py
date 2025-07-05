import smtplib
from email.mime.text import MIMEText

SMTP_HOST = 'localhost'
SMTP_PORT = 1025
FROM_EMAIL = 'admin@mad2.com'

def send_mail(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.send_message(msg)

from models import User
from app import app

with app.app_context():
    for user in User.query.all():
        send_mail(user.email, 'Vist the app', 'For the visit app?')
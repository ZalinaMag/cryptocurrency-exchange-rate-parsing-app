import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, RECIPIENT_EMAIL

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print("Письмо отправлено", flush=True)
    except Exception as e:
        print(f"Не удалось отправить письмо: {e}", flush=True)
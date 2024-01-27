# utils/email_service.py
import smtplib
from email.mime.text import MIMEText

class EmailService:
    def __init__(self, email_config):
        self.smtp_server = email_config["smtp_server"]
        self.smtp_port = email_config["smtp_port"]
        self.smtp_username = email_config["smtp_username"]
        self.smtp_password = email_config["smtp_password"]

    def send_confirmation_email(self, to_email, date, time, zoom_link):
        subject = "Zoom Meeting Confirmation"
        body = f"Your Zoom meeting is scheduled for {date} at {time}. Join using the link: {zoom_link}"

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.smtp_username
        msg["To"] = to_email

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.smtp_username, to_email, msg.as_string())

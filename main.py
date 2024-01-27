# main.py
from utils.zoom_api import ZoomAPI
from utils.email_service import EmailService

def main():
    # Replace these values with your actual credentials
    api_key = "YOUR_ZOOM_API_KEY"
    api_secret = "YOUR_ZOOM_API_SECRET"
    smtp_server = "your_smtp_server"
    smtp_port = 587  # Update with your SMTP port
    smtp_username = "your_username"
    smtp_password = "your_password"

    # Initialize Zoom API and Email Service
    zoom_api = ZoomAPI(api_key=api_key, api_secret=api_secret)
    email_service = EmailService(email_config={"smtp_server": smtp_server, "smtp_port": smtp_port, "smtp_username": smtp_username, "smtp_password": smtp_password})

    user_input = input("Enter your command: ")
    parsed_info = zoom_api.parse_input(user_input)

    if parsed_info:
        date, time, email = parsed_info
        join_link = zoom_api.schedule_meeting(date, time)
        email_service.send_confirmation_email(email, date, time, join_link)
        print(f"Zoom Meeting Scheduled! Zoom Link: {join_link}")
    else:
        print("Invalid command format. Please follow the specified format.")

if __name__ == "__main__":
    main()

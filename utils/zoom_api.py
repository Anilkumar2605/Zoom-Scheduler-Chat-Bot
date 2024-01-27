# utils/zoom_api.py
import requests
import re

class ZoomAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.zoom.us/v2"
        self.access_token = self.generate_access_token()

    def generate_access_token(self):
        # Zoom OAuth token endpoint
        token_url = "https://zoom.us/oauth/token"

        # OAuth token request payload
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        # Requesting the OAuth token
        response = requests.post(token_url, data=payload)

        if response.status_code == 200:
            # Successfully obtained the access token
            return response.json()["access_token"]
        else:
            # Failed to obtain the access token, handle the error
            raise Exception(f"Failed to obtain Zoom API access token: {response.text}")

    def parse_input(self, user_input):
        # Implement parsing logic to extract date, time, and email from user input
        # Replace this with your actual parsing logic
        match = re.match(r'Schedule a meeting on Zoom on (\d{2}-[A-Z]{3}-\d{4}) at (\d{2}:\d{2} [APMapm]{2}) with (\S+@\S+)', user_input)
        if match:
            date = match.group(1)
            time = match.group(2)
            email = match.group(3)
            return date, time, email
        else:
            return None

    def schedule_meeting(self, date, time):
        # Replace this with actual Zoom API integration code to schedule a meeting
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        payload = {
            "topic": "Scheduled Zoom Meeting",
            "start_time": f"{date}T{time}:00",
            "duration": 60,
            "settings": {
                "host_video": "true",
                "participant_video": "true",
                "join_before_host": "true",
            }
        }

        response = requests.post(f"{self.base_url}/users/me/meetings", headers=headers, json=payload)

        if response.status_code == 201:
            # Extract the join link from the response
            join_url = response.json()["join_url"]
            return join_url
        else:
            raise Exception(f"Failed to schedule Zoom meeting: {response.text}")

import os
import json
import gspread

from google.oauth2.service_account import Credentials
from config import GOOGLE_SHEET_ID

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def get_client():

    credentials_json = os.getenv("GOOGLE_CREDENTIALS")

    if credentials_json:

        credentials_info = json.loads(credentials_json)

        credentials = Credentials.from_service_account_info(
            credentials_info,
            scopes=SCOPES
        )

    else:

        credentials = Credentials.from_service_account_file(
            "credentials.json",
            scopes=SCOPES
        )

    return gspread.authorize(credentials)


client = get_client()

import time
from gspread.exceptions import APIError

for attempt in range(5):
    try:
        spreadsheet = client.open_by_key(GOOGLE_SHEET_ID)
        break
    except APIError as e:
        print(f"Google API unavailable. Retry {attempt + 1}/5")
        time.sleep(3)
else:
    raise Exception("Unable to connect to Google Sheets.")

def get_sheet(sheet_name):

    return spreadsheet.worksheet(sheet_name)


def get_records(sheet_name):

    return get_sheet(sheet_name).get_all_records()
import gspread

from google.oauth2.service_account import Credentials

from config import GOOGLE_SHEET_ID

SCOPES = [

    "https://www.googleapis.com/auth/spreadsheets",

    "https://www.googleapis.com/auth/drive"

]


credentials = Credentials.from_service_account_file(

    "credentials.json",

    scopes=SCOPES

)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(GOOGLE_SHEET_ID)


def get_sheet(sheet_name):

    return spreadsheet.worksheet(sheet_name)


def get_records(sheet_name):

    sheet = get_sheet(sheet_name)

    return sheet.get_all_records()
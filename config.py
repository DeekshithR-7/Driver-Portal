import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

DRIVER_SHEET = "Driver"

TRIP_SHEET = "Trip_Details"

BILLING_SHEET = "Monthly_Billing"

SITE_SHEET = "Site_Wise_Trips"
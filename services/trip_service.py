from config import TRIP_SHEET
from services.google_sheets import get_records


def to_float(value):
    try:
        if value in ("", None):
            return 0.0

        value = str(value)
        value = value.replace(",", "")
        value = value.replace("₹", "")

        return float(value)

    except:
        return 0.0


def to_int(value):
    try:
        if value in ("", None):
            return 0

        return int(float(value))

    except:
        return 0


def get_all_trips():

    return get_records(TRIP_SHEET)


def map_trip(row):

    return {

        "billing_month": row.get("Billing Month", ""),

        "trip_date": row.get("Trip Date", ""),

        "trip_id": row.get("Trip ID", ""),

        "driver_id": row.get("Driver ID", ""),

        "driver_name": row.get("Driver Name", ""),

        "mobile": row.get("Mobile No", ""),

        "vehicle_no": row.get("Vehicle No", ""),

        "vehicle_type": row.get("Vehicle Type", ""),

        "site_name": row.get("Site Name", ""),

        "shift": row.get("Shift Time", ""),

        "trip_type": row.get("Trip Type", ""),

        "location": row.get("Location", ""),

        "rate_type": row.get("Rate Type", ""),

        "employees": to_int(
            row.get("Emp Count")
        ),

        "escort": row.get("Escort (Y/N)", ""),

        "kms": to_float(
            row.get("KMs")
        ),

        "trip_rate": to_float(
            row.get("Trip Rate")
        ),

        "escort_rate": to_float(
            row.get("Escort Rate")
        ),

        "delay_login": to_float(
            row.get("Delay Login Amount")
        ),

        "uniform_penalty": to_float(
            row.get("No Uniform Penalty")
        ),

        "ehs_penalty": to_float(
            row.get("EHS Penalty")
        ),

        "other_penalty": to_float(
            row.get("Other Penalty Amount")
        ),

        "status": row.get("Trip Status", ""),

        "complaint": row.get("Driver Complaint", ""),

        "complaint_remarks": row.get(
            "Complaint Remarks",
            ""
        ),

        "complaint_status": row.get(
            "Complaint Status",
            ""
        ),

        "admin_remarks": row.get(
            "Admin Remarks",
            ""
        )

    }


def get_driver_trips(driver_id):

    driver_id = str(driver_id).strip()

    trips = []

    for row in get_all_trips():

        if str(row.get("Driver ID", "")).strip() == driver_id:

            trips.append(
                map_trip(row)
            )

    return trips
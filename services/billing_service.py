from config import BILLING_SHEET
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


def get_all_billing():

    return get_records(BILLING_SHEET)


def map_bill(row):

    return {

        "billing_id": row.get("Billing ID", ""),

        "billing_month": row.get("Billing Month", ""),

        "driver_id": row.get("Driver ID", ""),

        "driver_name": row.get("Driver Name", ""),

        "mobile": row.get("Mobile No", ""),

        "vehicle_no": row.get("Vehicle No", ""),

        "total_trips": to_int(
            row.get("Total Trips")
        ),

        "gross_amount": to_float(
            row.get("Total Bill Amount")
        ),

        "diesel": to_float(
            row.get("Diesel Amount")
        ),

        "advance": to_float(
            row.get("Advance Amount")
        ),

        "penalty": to_float(
            row.get("Penalty Amount")
        ),

        "three_percent": to_float(
            row.get("3% (Diesel /Advance)")
        ),

        "gps": to_float(
            row.get("GPS Rental")
        ),

        "other": to_float(
            row.get("Other Deductions")
        ),

        "final_amount": to_float(
            row.get("Final Bill Amount")
        ),

        "driver_confirmation": row.get(
            "Driver Confirmation",
            ""
        ),

        "driver_remarks": row.get(
            "Driver Remarks",
            ""
        ),

        "complaint_status": row.get(
            "Complaint Status",
            ""
        ),

        "payment_status": row.get(
            "Payment Status",
            ""
        ),

        "hold_reason": row.get(
            "Hold Reason",
            ""
        ),

        "payment_date": row.get(
            "Payment Date",
            ""
        ),

        "payment_reference": row.get(
            "Payment Reference",
            ""
        ),

        "admin_remarks": row.get(
            "Admin Remarks",
            ""
        )

    }


def get_driver_billing(driver_id):

    driver_id = str(driver_id).strip()

    for row in get_all_billing():

        if str(row.get("Driver ID", "")).strip() == driver_id:

            return map_bill(row)

    return None

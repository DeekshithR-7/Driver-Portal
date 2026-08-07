from config import DRIVER_SHEET
from services.google_sheets import get_records


def normalize_phone(phone):
    """
    Converts any phone number to a standard 10-digit format.
    """

    if phone is None:
        return ""

    phone = str(phone).strip()

    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")
    phone = phone.replace("+91", "")

    if phone.startswith("91") and len(phone) == 12:
        phone = phone[2:]

    return phone


def is_valid_phone(phone):

    phone = normalize_phone(phone)

    return len(phone) == 10 and phone.isdigit()


def get_all_drivers():

    return get_records(DRIVER_SHEET)


def map_driver(row):

    return {

        "driver_id": row.get("Driver ID", ""),

        "driver_name": row.get("Driver Name", ""),

        "mobile": normalize_phone(
            row.get("Mobile Number", "")
        ),

        "alternate_mobile": normalize_phone(
            row.get("Alternate Mobile No", "")
        ),

        "vehicle_no": row.get("Vehicle Number", ""),

        "vehicle_type": row.get("Vehicle Type", ""),

        "joining_date": row.get("Joining Date", ""),

        "aadhar": row.get("Aadhar Naumber", ""),

        "pan": row.get("Pan Number", ""),

        "dl_no": row.get("D L No", ""),

        "dl_expiry": row.get("D L Expiry Date", ""),

        "bank_holder": row.get(
            "Bank Account Holder Name",
            ""
        ),

        "bank_account": row.get(
            "Bank Account No",
            ""
        ),

        "ifsc": row.get(
            "IFSD Code",
            ""
        ),

        "bank_name": row.get(
            "Bank Name",
            ""
        ),

        "upi": row.get(
            "UPI ID",
            ""
        ),

        "payment_mode": row.get(
            "Payment Mode",
            ""
        ),

        "status": row.get(
            "Driver Status",
            ""
        ),

        "remarks": row.get(
            "Remarks",
            ""
        )

    }


def get_driver_by_phone(phone):

    phone = normalize_phone(phone)

    for row in get_all_drivers():

        sheet_phone = normalize_phone(
            row.get("Mobile Number", "")
        )

        if sheet_phone == phone:

            return map_driver(row)

    return None


def get_driver_by_id(driver_id):

    driver_id = str(driver_id).strip()

    for row in get_all_drivers():

        if str(row.get("Driver ID", "")).strip() == driver_id:

            return map_driver(row)

    return None
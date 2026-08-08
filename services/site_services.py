from config import SITE_SHEET

from services.google_sheets import get_records


def to_int(value):

    try:
        return int(float(value))

    except:
        return 0


def to_float(value):

    try:
        return float(value)

    except:
        return 0.0


def get_all_site_records():

    return get_records(SITE_SHEET)


def map_site(row):

    return {

        "billing_month": row.get(
            "Billing Month",
            ""
        ),

        "driver_id": row.get(
            "Driver ID",
            ""
        ),

        "driver_name": row.get(
            "Driver Name",
            ""
        ),

        "mobile": row.get(
            "Mobile Number",
            ""
        ),

        "vehicle_no": row.get(
            "Vehicle Number",
            ""
        ),

        "vehicle_type": row.get(
            "Vehicle Type",
            ""
        ),

        "site_name": row.get(
            "Site Name",
            ""
        ),

        "trip_count": to_int(
            row.get("Trip Count")
        ),

        "escort_count": to_int(
            row.get("Escort Count")
        ),

        "trip_amount": to_float(
            row.get("Trip Amount")
        ),

        "escort_amount": to_float(
            row.get("Escort Amount")
        ),

        "penalty": to_float(
            row.get("Penalty Amount")
        ),

        "other_amount": to_float(
            row.get("Other Amount (+/-)")
        ),

        "net_amount": to_float(
            row.get("Net Site Amount")
        ),

        "remarks": row.get(
            "Remarks",
            ""
        )

    }


def get_driver_site_summary(driver_id):

    driver_id = str(driver_id).strip()

    records = get_all_site_records()

    results = []

    for row in records:

        if str(
            row.get(
                "Driver ID",
                ""
            )
        ).strip() == driver_id:

            results.append(
                map_site(row)
            )

    return results
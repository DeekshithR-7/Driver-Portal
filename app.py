from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from config import SECRET_KEY

from services.driver_service import (
    get_driver_by_phone,
    get_driver_by_id,
    is_valid_phone
)

from services.trip_service import (
    get_driver_trips
)

from services.billing_service import (
    get_driver_billing
)

app = Flask(__name__)

app.secret_key = SECRET_KEY


# ==========================================
# LOGIN
# ==========================================

@app.route("/", methods=["GET", "POST"])
def login():

    if session.get("driver_id"):
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        if not is_valid_phone(phone):

            flash(
                "Please enter a valid mobile number."
            )

            return render_template(
                "login.html"
            )

        driver = get_driver_by_phone(phone)

        if driver is None:

            flash(
                "Driver not found."
            )

            return render_template(
                "login.html"
            )

        session.clear()

        session["driver_id"] = driver["driver_id"]

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "login.html"
    )


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    if "driver_id" not in session:

        return redirect(url_for("login"))

    driver = get_driver_by_id(
        session["driver_id"]
    )

    bill = get_driver_billing(
        session["driver_id"]
    )

    trips = get_driver_trips(
        session["driver_id"]
    )

    return render_template(

        "dashboard.html",

        driver=driver,

        bill=bill,

        trips=trips[:10]

    )


# ==========================================
# BILLING
# ==========================================

@app.route("/billing")
def billing():

    if "driver_id" not in session:
        return redirect(url_for("login"))

    bill = get_driver_billing(
        session["driver_id"]
    )

    if bill is None:
        flash("Billing not found.")
        return redirect(url_for("dashboard"))

    return render_template(
        "billing.html",
        bill=bill
    )
# ==========================================
# TRIPS
# ==========================================

@app.route("/trips")
def trips():

    if "driver_id" not in session:

        return redirect(url_for("login"))

    trips = get_driver_trips(
        session["driver_id"]
    )

    return render_template(

        "trips.html",

        trips=trips

    )


# ==========================================
# PROFILE
# ==========================================

@app.route("/profile")
def profile():

    if "driver_id" not in session:

        return redirect(url_for("login"))

    driver = get_driver_by_id(
        session["driver_id"]
    )

    return render_template(

        "profile.html",

        driver=driver

    )


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
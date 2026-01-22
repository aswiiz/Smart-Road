from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in production

reports = []

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        desc = request.form.get("desc")
        name = request.form.get("name")
        address = request.form.get("address")
        district = request.form.get("district")
        state = request.form.get("state")
        panchayath = request.form.get("panchayath")
        location = request.form.get("location")

        report_id = str(uuid.uuid4())[:6].upper()

        report = {
            "id": report_id,
            "id": report_id,
            "location": location,
            "name": name,
            "address": address,
            "district": district,
            "state": state,
            "panchayath": panchayath,
            "desc": desc,
            "status": "Pending",
            "time": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        reports.append(report)
        message = f"Report submitted successfully. Your ID is {report_id}"

    return render_template("index.html", message=message)


@app.route("/track", methods=["POST"])
def track():
    rid = request.form.get("rid").upper()
    result = None

    for r in reports:
        if r["id"] == rid:
            result = r
            break

    return render_template("index.html", result=result)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Hardcoded credentials for authority
        if username == "admin" and password == "admin123":
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid Credentials. Please try again."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard.html", reports=reports)


@app.route("/update_status/<report_id>", methods=["POST"])
def update_status(report_id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    new_status = request.form.get("status")
    for r in reports:
        if r["id"] == report_id:
            r["status"] = new_status
            break
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)

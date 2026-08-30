from flask import Flask, jsonify, render_template

from app.monitoring.health_checker import check_application

from app.incidents.incident_manager import (
    create_incident,
    resolve_current_incident
)


app = Flask(__name__)

URL = "http://127.0.0.1:9999/health"


@app.route("/")
def home():

    result = check_application(URL)

    incident = None

    if result["status"] == "DOWN":

        incident = create_incident(
            "Demo Application",
            result["error"]
        )

    else:

        resolve_current_incident("Demo Application")

    return render_template(
        "dashboard.html",
        monitoring=result,
        incident=incident
    )


@app.route("/dashboard")
def dashboard():

    result = check_application(URL)

    incident = None

    if result["status"] == "DOWN":

        incident = create_incident(
            "Demo Application",
            result["error"]
        )

    else:

        resolve_current_incident("Demo Application")

    return render_template(
        "dashboard.html",
        monitoring=result,
        incident=incident
    )


@app.route("/monitor")
def monitor():

    result = check_application(URL)

    if result["status"] == "DOWN":

        incident = create_incident(
            "Demo Application",
            result["error"]
        )

        return jsonify({
            "monitoring": result,
            "incident": incident
        })

    resolved_incident = resolve_current_incident(
        "Demo Application"
    )

    return jsonify({
        "monitoring": result,
        "incident": None,
        "resolved_incident": resolved_incident
    })


if __name__ == "__main__":
    app.run(debug=True)
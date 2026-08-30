from app.incidents.incident_manager import create_incident


def test_create_incident():
    incident = create_incident(
        "Demo Application",
        "Connection refused"
    )

    assert incident["service"] == "Demo Application"
    assert incident["error"] == "Connection refused"
    assert incident["status"] == "OPEN"

test_create_incident()
print("Incident test passed successfully!")
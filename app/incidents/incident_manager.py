from app.database.database import (
    save_incident,
    get_open_incident,
    resolve_incident
)


def create_incident(service, error):

    existing_incident = get_open_incident(service)

    if existing_incident:
        return {
            "id": existing_incident[0],
            "service": existing_incident[1],
            "error": existing_incident[2],
            "status": existing_incident[3]
        }

    status = "OPEN"

    save_incident(service, error, status)

    incident = get_open_incident(service)

    return {
        "id": incident[0],
        "service": incident[1],
        "error": incident[2],
        "status": incident[3]
    }


def resolve_current_incident(service):

    incident = resolve_incident(service)

    if incident:
        return {
            "id": incident[0],
            "service": incident[1],
            "error": incident[2],
            "status": incident[3]
        }

    return None
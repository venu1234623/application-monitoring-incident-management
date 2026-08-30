import sqlite3


def create_database():
    connection = sqlite3.connect("incidents.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            error TEXT,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_incident(service, error, status):
    connection = sqlite3.connect("incidents.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO incidents (service, error, status)
        VALUES (?, ?, ?)
        """,
        (service, error, status)
    )

    connection.commit()
    connection.close()


def get_open_incident(service):
    connection = sqlite3.connect("incidents.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, service, error, status
        FROM incidents
        WHERE service = ? AND status = 'OPEN'
        ORDER BY id DESC
        LIMIT 1
        """,
        (service,)
    )

    incident = cursor.fetchone()

    connection.close()

    return incident


def resolve_incident(service):
    connection = sqlite3.connect("incidents.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE incidents
        SET status = 'RESOLVED'
        WHERE service = ? AND status = 'OPEN'
        """,
        (service,)
    )

    connection.commit()

    cursor.execute(
        """
        SELECT id, service, error, status
        FROM incidents
        WHERE service = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (service,)
    )

    incident = cursor.fetchone()

    connection.close()

    return incident
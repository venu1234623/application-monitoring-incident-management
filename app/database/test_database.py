import sqlite3

connection = sqlite3.connect("incidents.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM incidents")

incidents = cursor.fetchall()

for incident in incidents:
    print(incident)

connection.close()

print("Database test passed successfully!")
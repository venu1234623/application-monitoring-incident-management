import requests
import time


def check_application(url):
    start_time = time.time()

    try:
        response = requests.get(url, timeout=5)

        response_time = round((time.time() - start_time) * 1000, 2)

        if response.status_code == 200:
            return {
                "status": "UP",
                "status_code": response.status_code,
                "response_time_ms": response_time
            }

        return {
            "status": "DOWN",
            "status_code": response.status_code,
            "response_time_ms": response_time
        }

    except requests.exceptions.RequestException as error:
        response_time = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "DOWN",
            "status_code": None,
            "response_time_ms": response_time,
            "error": str(error)
        }
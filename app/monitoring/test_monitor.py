from app.monitoring.health_checker import check_application


def test_application_is_up():
    url = "http://127.0.0.1:9999/health"

    result = check_application(url)

    assert result["status"] == "UP"
    assert result["status_code"] == 200 

def test_application_is_down():
    url = "http://127.0.0.1:9999/wrong"

    result = check_application(url)

    assert result["status"] == "DOWN"
    assert result["status_code"] == 404    

test_application_is_up()
test_application_is_down()

print("Monitoring tests passed successfully!")
import requests

def test_check_header():
    expected_header_name = "x-secret-homework-header"
    expected_value = "Some secret value"

    response = requests.get("https://playground.learnqa.ru/api/homework_header")

    headers = response.headers
    print(f"Headers received in response: {headers}")

    assert expected_header_name in headers, f"Header '{expected_header_name}' not found in response"

    actual_value = headers[expected_header_name]
    print(f"Value of '{expected_header_name}' header is '{actual_value}'")

    assert actual_value == expected_value, \
        f"Header value '{actual_value}' does not match the expected value '{expected_value}'"
import requests

def test_check_cookie():
    expected_cookie_name = "HomeWork"
    expected_value = "hw_value"

    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

    cookies = response.cookies.get_dict()
    print(f"Cookies received in response: {cookies}")

    assert expected_cookie_name in cookies, f"Cookie '{expected_cookie_name}' not found in response"

    actual_value = cookies[expected_cookie_name]
    print(f"Value of '{expected_cookie_name}' cookie is {actual_value}")

    assert actual_value == expected_value, \
        f"Cookie value {actual_value} does not match the expected value {expected_value}"
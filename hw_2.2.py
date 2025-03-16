import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

redirect_count = len(response.history)

print(f"Total redirects: {redirect_count}")
print(f"Final URL: {response.url}")
import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# Create task
response = requests.get(url)
result_when_creating_task = response.json()

token = result_when_creating_task['token']
seconds = result_when_creating_task['seconds']
print(f"Task created with token {token}, it will be ready in {seconds} seconds")


# Check status when task is not ready
payload = {"token": token}
response = requests.get(url, params=payload)
result_when_task_not_ready = response.json()

status = result_when_task_not_ready['status']
print(f"Status when task is not ready: {status}")

if status != "Job is NOT ready":
    print(f"Unexpected status value: {status}")


# Wait until task is ready
time.sleep(seconds)


# Check status when task is ready
response = requests.get(url, params=payload)
result_when_task_is_ready = response.json()

status = result_when_task_is_ready['status']
print(f"Status when task is ready: {status}")

if status != "Job is ready":
    print(f"Unexpected status value: {status}")

result = result_when_task_is_ready['result']

if 'result' in result_when_task_is_ready:
    print(f"Result is {result}")
else:
    print("There is no 'result' field in the response")


# Check error when using wrong token
payload = {"token": "None"}
response = requests.get(url, params=payload)
result_with_wrong_token = response.json()

error = result_with_wrong_token['error']
print(f"Error message when using wrong token: {error}")

import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
methods = ["GET", "POST", "PUT", "DELETE"]


response = requests.get(url)

response = requests.patch(url, data={"method": "PATCH"})

response = requests.get(url, params={"method": "GET"})
response = requests.post(url, data={"method": "POST"})
response = requests.put(url, data={"method": "PUT"})
response = requests.delete(url, data={"method": "DELETE"})


for method in methods:
    for method_param in methods:
        response = requests.request(method, url,
                                    params={"method": method_param} if method == "GET" else {},
                                    data={"method": method_param} if method != "GET" else {})

        if ((method == method_param and response.text != '{"success":"!"}')
                or (method != method_param and response.text == '{"success":"!"}')):
            print(f"HTTP method {method} does not match the method parameter {method_param}, "
                  f"but the successful response was received. Response: {response.text}")

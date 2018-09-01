import requests
response = requests.get("http://www.baidu.com")
#print(response.text)
#print(response.headers)
print(response.status_code)
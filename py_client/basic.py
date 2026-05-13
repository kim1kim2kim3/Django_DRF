import requests

endpoint = "https://httpbin.org/anything"


get_response = requests.get(endpoint)

print(f"get_response: {get_response}")
print("--------------------------------")
print(f"text: {get_response.text}") # print raw text response
print("--------------------------------")
print(f"status_code: {get_response.status_code}")
print("--------------------------------")
print(f"json: {get_response.json()}") # print json response 


""" get_response: <Response [200]>
--------------------------------
text: {
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.34.0",
    "X-Amzn-Trace-Id": "Root=1-6a0432ad-5d18f2261a5cfba4281e81fb"
  },
  "json": null,
  "method": "GET",
  "origin": "164.125.223.35",
  "url": "https://httpbin.org/anything"
}

--------------------------------
status_code: 200
--------------------------------
json: {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.0', 
'X-Amzn-Trace-Id': 'Root=1-6a0432ad-5d18f2261a5cfba4281e81fb'}, 'json': None, 'method': 'GET', 'origin': '164.125.223.35', 'url': 'https://httpbin.org/anything'} """



get_response = requests.get(endpoint, json={"query": "Hello World"})

print(f"get_response: {get_response}")
print("--------------------------------")
print(f"text: {get_response.text}") # print raw text response
print("--------------------------------")
print(f"status_code: {get_response.status_code}")
print("--------------------------------")
print(f"json: {get_response.json()}") # print json response 


""" get_response: <Response [200]>
--------------------------------
text: {
  "args": {},
  "data": "{\"query\": \"Hello World\"}", data부분에 값이 들어가 있음
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "24",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.34.0",
    "X-Amzn-Trace-Id": "Root=1-6a0434c6-5b778c4203131b12700cd91e"
  },
  "json": {
    "query": "Hello World"
  },
  "method": "GET",
  "origin": "164.125.223.35",
  "url": "https://httpbin.org/anything"
}

--------------------------------
status_code: 200
--------------------------------
json: {'args': {}, 'data': '{"query": "Hello World"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '24', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.0', 'X-Amzn-Trace-Id': 'Root=1-6a0434c6-5b778c4203131b12700cd91e'}, 'json': {'query': 'Hello World'}, 'method': 'GET', 'origin': '164.125.223.35', 'url': 'https://httpbin.org/anything'}
 """




get_response = requests.get(endpoint, params={"query": "Hello World"})
print(f"get_response: {get_response}")
print("--------------------------------")
print(f"text: {get_response.text}") # print raw text response
print("--------------------------------")
print(f"status_code: {get_response.status_code}")
print("--------------------------------")
print(f"json: {get_response.json()}") # print json response  


""" 
get_response: <Response [200]>
--------------------------------
text: {
  "args": {
    "query": "Hello World"          args 부분에 값이 들어가 있음
  },
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.34.0",
    "X-Amzn-Trace-Id": "Root=1-6a04355a-619203250693d1bd176a0abe"
  },
  "json": null,
  "method": "GET",
  "origin": "164.125.223.35",
  "url": "https://httpbin.org/anything?query=Hello+World"
}

--------------------------------
status_code: 200
--------------------------------
json: {'args': {'query': 'Hello World'}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.0', 'X-Amzn-Trace-Id': 'Root=1-6a04355a-619203250693d1bd176a0abe'}, 'json': None, 'method': 'GET', 'origin': '164.125.223.35', 'url': 'https://httpbin.org/anything?query=Hello+World'}
"""


get_response = requests.get(endpoint, data={"query": "Hello World"})
print(f"get_response: {get_response}")
print("--------------------------------")
print(f"text: {get_response.text}") # print raw text response
print("--------------------------------")
print(f"status_code: {get_response.status_code}")
print("--------------------------------")
print(f"json: {get_response.json()}") # print json response  


"""
get_response: <Response [200]>
--------------------------------
text: {
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "query": "Hello World"           form 부분에 값이 들어가 있음
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "17",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.34.0",
    "X-Amzn-Trace-Id": "Root=1-6a043641-291eaf37383f405022ddeeea"
  },
  "json": null,
  "method": "GET",
  "origin": "164.125.223.35",
  "url": "https://httpbin.org/anything"
}

--------------------------------
status_code: 200
--------------------------------
json: {'args': {}, 'data': '', 'files': {}, 'form': {'query': 'Hello World'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '17', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.0', 'X-Amzn-Trace-Id': 'Root=1-6a043641-291eaf37383f405022ddeeea'}, 'json': None, 'method': 'GET', 'origin': '164.125.223.35', 'url': 'https://httpbin.org/anything'}
"""



endpoint = "http://127.0.0.1:8000/"

get_response = requests.get(endpoint)
print(f"get_response: {get_response}")
print("--------------------------------")
print(f"text: {get_response.text}") # print raw text response
print("--------------------------------")
print(f"status_code: {get_response.status_code}")
print("--------------------------------")




endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint)
print(f"get_response: {get_response}")
print("--------------------------------")
print(f"text: {get_response.text}") # print raw text response
print("--------------------------------")
print(f"status_code: {get_response.status_code}")
print("--------------------------------")
print(f"json: {get_response.json()}") # print json response
print("--------------------------------")
print(f"message: {get_response.json()['message']}")



""" 
get_response: <Response [200]>
--------------------------------
text: {"message": "Hi there, this is your Django API response"}
--------------------------------
status_code: 200
--------------------------------
json: {'message': 'Hi there, this is your Django API response'}
--------------------------------
message: Hi there, this is your Django API response 
"""
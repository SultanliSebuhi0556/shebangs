import requests as _client

headers = { "User-Agent": "my-python-app/1.0 (your_email@example.com)" }

while(True):
    search = input("Seach: ").strip().replace(" ", "+")
    if not search: print("Please enter what you are searching for!"); continue
    break

search_url = f"https://en.wikipedia.org/w/rest.php/v1/search/title?q={search}&limit=10"
search_response = _client.get(search_url, headers=headers)
if(search_response.status_code != 200): print(f"Request didm't succeed! Status code : {search_response.status_code}")

search_result = search_response.json()['pages'][:25]

print("Choice one below:")
response_length = len(search_result)
for i in range(0, response_length): print(f"{i}) " + search_result[i]['title'])

while(True):
    try: user_input = int(input(f"Choice 0-{response_length-1}: "))
    except: print("Please inseart a number!"); continue
    if (user_input < 0 or user_input > response_length-1): print(f"Please inseart a number between 0 and {response_length-1}!"); continue
    break

summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{search_result[user_input]['key']}"
response = _client.get(summary_url, headers=headers)
if(response.status_code != 200): print(f"Request didm't succeed! Status code : {response.status_code}")

print("\n" + response.json()['extract'] + "\n")
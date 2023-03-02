import requests

url = input("Please enter a URL: ")

with requests.get(url) as response:
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
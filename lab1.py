import requests
import datetime

url = input("Please enter a URL: ")

with requests.get(url) as response:
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    print("\nThe Web Server is running", response.headers['Server'])

    if not response.cookies.get_dict():
        print("The page does not use Cookies")
    else:
        print("The page also uses Cookies, such as:")
        for cookie in response.cookies:
            if cookie.expires == None:
                print(f"{cookie.name}: Expired")
            else:
                expiration = datetime.datetime.fromtimestamp(cookie.expires)
                print(f"{cookie.name}: Valid until {expiration}")
        print("")

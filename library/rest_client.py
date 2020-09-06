import requests
from config import rest_server_base_url


def authenticate(id):
    url = rest_server_base_url + 'auth/' + id
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    if (response.status_code == 200):
        print("ID: ", id, " Accepted")
        return True
    else:
        print("ID: ", id, "Access Denied")
        return False

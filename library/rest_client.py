import requests
from config import rest_server_base_url
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def authenticate(id):
    url = rest_server_base_url + 'auth/' + id
    print(url)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload,
                                verify=False)   # Disbales SSL verification

    if (response.status_code == 200):
        print("ID: ", id, " Accepted")
        return True
    else:
        print("ID: ", id, "Access Denied")
        return False

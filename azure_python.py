from sys import stdin

from requests import codes, get
from yaml import safe_load

def main():
    print("Azure Python")
    conf = safe_load(stdin)
    subscriptionId = conf["subscriptionId"]
    uri = "https://management.azure.com/subscriptions/" + subscriptionId + \
        "/locations?api-version=2022-12-01"
    token = conf["token"]
    headers = { "Authorization": "Bearer " + token}
    response = get(uri, headers=headers)
    if response.status_code == codes.OK:
        print(response)
    else:
        request = response.request
        print(request.method + " " + request.url)
        print(str(response.status_code) + " " + response.reason)
    print(USAGE)

USAGE = """\
usage: python azure_python.py
where
  - "python" is the Python runtime
"""

if __name__ == "__main__":
    main()

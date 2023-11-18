from sys import stdin

from requests import codes, get, post
from yaml import safe_load

USAGE = """\
usage: python azure_python.py
where
  - "python" is the Python runtime
"""

def main():
    HOST_LOGIN = "https://login.microsoftonline.com/"
    HOST_MANAGE = "https://management.azure.com/"
    print("Azure Python")
    conf = safe_load(stdin)

    access_token = conf["access_token"]
    if (len(access_token) == 0):
        tenant_id = conf["tenant_id"]
        client_id = conf["client_id"]
        secret = conf["secret"]
        uri = HOST_LOGIN + tenant_id + "/oauth2/v2.0/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "client_id": client_id,
            "scope": HOST_MANAGE + ".default",
            "client_secret": secret,
            "grant_type": "client_credentials"
        }
        response = post(uri, data, headers=headers)
        if response.status_code == codes.OK:
            # TODO check token_type Bearer
            print(response.text)
        else:
            request = response.request
            print(request.method + " " + request.url)
            print(str(response.status_code) + " " + response.reason)
            print(response.text)

    subscription_id = conf["subscription_id"]
    uri = HOST_MANAGE + "subscriptions/" + subscription_id + \
        "/locations?api-version=2022-12-01"
    headers = {"Authorization": "Bearer " + access_token}
    response = get(uri, headers=headers)
    if response.status_code == codes.OK:
        print(response.text)
    else:
        request = response.request
        print(request.method + " " + request.url)
        print(str(response.status_code) + " " + response.reason)
        print(response.text)
    
    print(USAGE)

if __name__ == "__main__":
    main()

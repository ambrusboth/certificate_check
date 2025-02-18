import os

import certifi
import requests

if __name__ == "__main__":
    ENV_KEY = "REQUESTS_CA_BUNDLE"
    if ENV_KEY not in os.environ:
        os.environ[ENV_KEY] = certifi.where()
    print(f"{ENV_KEY} = '{os.environ[ENV_KEY]}'")

    URL = "https://example.com/api/endpoint"
    response = requests.get(URL, verify=certifi.where(), timeout=30)
    print(response.status_code)

import os

import certifi
import requests

if __name__ == "__main__":
    ENV_KEY = "REQUESTS_CA_BUNDLE"
    if ENV_KEY not in os.environ:
        os.environ[ENV_KEY] = certifi.where()
    print(f"{ENV_KEY} = '{os.environ[ENV_KEY]}'")

    # URL = "https://example.com/api/endpoint"
    # URL = "https://api.github.com"
    URL = "https://official-joke-api.appspot.com/random_joke"
    # URL = "https://dog.ceo/api/breeds/image/random"
    # URL = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"  # This works in the browser but not in the code
    response = requests.get(
        URL,
        verify=certifi.where(),
        #    cert="C:\\Users\\a0102487\\Downloads\\zscaler_try.cer",
        timeout=30,
    )
    print(response.status_code)
    print(response.text)

from pprint import pprint

import requests


def send_message(token, channel, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={channel}&text="

    response = requests.get(f"{url}{text}")
    if response.status_code == 200:
        pprint(response.json())
    else:
        print(response.text)


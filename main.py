from requests import Session
import json
from anti_useragent import UserAgent as ua

def main(email):

    userAgent = ua().random

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://argentlabs.typeform.com",
        "referer": "https://argentlabs.typeform.com/to/isyBIKXh",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": userAgent
    }

    variable = Session()
    
    variable.get("https://argentlabs.typeform.com/forms/isyBIKXh", headers=headers)

    response = variable.post("https://argentlabs.typeform.com/forms/isyBIKXh/start-submission", headers=headers)
    js_answer = response.json()

    datas = {
        "signature": js_answer["signature"],
        "form_id": "isyBIKXh",
        "landed_at": js_answer["submission"]["landed_at"],
        "answers": [
            {
                "field": {
                    "id": "Zu6yOpt4sbcG",
                    "type": "email"
                },
                "type": "email",
                "email": email
            }
        ],
        "thankyou_screen_ref": "01FMMMMTDWE6245RSSQX0FZM7Y"
        }  

    response = variable.post("https://argentlabs.typeform.com/forms/isyBIKXh/complete-submission", headers=headers, json=datas)

    if response.status_code != 200:
        print(f"FAIL to register {email}, status code: {response.status_code}")
    else:
        print(f"{email} successfully registered!")    



if __name__ == "__main__":
    with open("emails.txt") as f:
        emails = f.read().splitlines()

    for email in emails:
        main(email)

    print("GG WP!")
import requests
from datetime import datetime, timedelta

USERNAME = "glebka"
GRAPH_ID = "ggwp420"
TOKEN = "r0238uv023475n9yrj"
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Gamin Time",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime.now() - timedelta(days=1)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes you have played today?: ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.json())
## UPDATE
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


update_config = {
    "quantity": "150"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)
## DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.json())

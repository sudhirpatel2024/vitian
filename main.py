import json
import requests
def getting_ip(row):
    """This function calls the api and return the response"""
    url = f"https://api.ipbase.com/v2/info?apikey=idfEJs8hwZXCnuu75DlhJYOzdBhBHzKYcGWdH8w6&language=en&ip={row}"       # getting records from getting ip address
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers)
    respond = json.loads(response.text)
    print(respond["data"]["location"]["region"]["name"])
    return respond

getting_ip("43.205.197.227")
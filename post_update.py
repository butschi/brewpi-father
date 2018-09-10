import json
import requests

brewpi_url = 'http://brewpi.local/socketmessage.php'
brewfather_url = 'http://log.brewfather.net/brewpiless?id=XXXXXXXXXXXXXX'


def get_brewdata():
    response = requests.post(
        brewpi_url,
        data={'messageType': 'getTemperatures'}
    )

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def post_brewdata(data):
    response = requests.post(
        brewfather_url,
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print(response)
        return None


def map_brewdata(data):
    return dict(
        id='1',
        fridgeSet=data.get('FridgeSet'),
        beerTemp=data.get('BeerTemp'),
        beerSet=data.get('BeerSet'),
        fridgeTemp=data.get('FridgeTemp')
    )


brewdata = get_brewdata()

if brewdata is not None:
    print("Current temperatures: ")
    print(brewdata)
    result = post_brewdata(map_brewdata(brewdata))

    print(result)

else:
    print('[!] Request Failed')

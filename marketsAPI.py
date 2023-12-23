import json
from json import JSONDecodeError
from requests import get

# CSGOMARKET API
def getItemList(currency : str) -> dict:
    return getAPIResponse(url=f'https://market.csgo.com/api/v2/prices/{currency}.json',
                          error='CSGOMarket')['items']

# CSGOBACKPACK API
def getItem(item : str, currency : str) -> dict:
    return getAPIResponse(url=f'https://csgobackpack.net/api/GetItemPrice/?time=2&extend=true&currency={currency}&id={item}',
                          error="CSGOBackpack")
    
def getAPIResponse(url : str, error : str):
    response = get(url=url)
    try:
        data = json.loads(response.text)
    except JSONDecodeError:
        print(f'  {error} API Error')
        raise exit()
    
    if checkSuccess(data):
        return data
    else:
        print(f'  {error} API Error')
        raise exit()

def checkSuccess(data : dict) -> bool:
    return data['success']
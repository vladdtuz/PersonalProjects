

def salvage(Option):
    """
    Function to return basic information regarding salvage kits

    Input:
    - Item ID

    Output:
    - price per use
    """
    crude = {'price': 2.13, 'chance of rarer':0 ,'change of upgrades':5}
    basic = {'price': 3.52, 'chance of rarer':10 ,'change of upgrades':20}
    fine = {'price': 11.52, 'chance of rarer':15 ,'change of upgrades':40}
    journeyman = {'price': 32, 'chance of rarer':20 ,'change of upgrades':60}
    master = {'price': 61.44, 'chance of rarer':25,'change of upgrades':80}
    mystic = {'price': 10.5, 'chance of rarer':25,'change of upgrades':80}
    kits = [crude,basic,fine,journeyman,master,mystic]
    
    return(kits[Option]['price'])

def sell(ID):
    """
    Function to provide listing data for the requested item
    Input:
    - item ID

    Output:
    - selling listings
    """
    import requests,json
    url = "https://api.guildwars2.com/v2/commerce/listings/"+str(ID)
    selling = json.loads(requests.get(url).text)

    return selling['sells']

def buy(ID):
    """
    Function to provide listing data for the requested item
    Input:
    - item ID

    Output:
    - buying listings
    """
    import requests,json
    url = "https://api.guildwars2.com/v2/commerce/listings/"+str(ID)
    buying = json.loads(requests.get(url).text)

    return buying['buys']
    
def item(ID):
    import requests,json
    url ="https://api.guildwars2.com/v2/items/" +str(ID)
    info = json.loads(requests.get(url).text)

    return info

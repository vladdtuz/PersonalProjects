

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

def Profit(Price):
    '''
    Function to determine profit after tax
    Input:
    - item price
    Output:
    - profit after tax
    '''
    return (Price-Price*0.15)

def SalvageDrops(weight,ArmourType):
        '''
        Function to return salvage rates based on emperical data
        Salavage rates based on armour type and classification
        Input:
        - weight : heavy, medium or light
        - ArmourType:helm, shoulder, coat,gloves,leggings,boots
        Output:
        - single number; salvage drop rate
        '''


        Heavy = {'Helm': 1.35, 'Shoulder': 1.08, 'Coat':1.88,
        'Gloves':1.18,'Leggings':1.1, 'Boots': 1.17}

        Medium = {'Helm': 1.8, 'Shoulder': 1.78, 'Coat':2.45,
        'Gloves':1.82,'Leggings':1.69, 'Boots': 1.81,'Back item':1.7}

        Light = {'Helm': 1.81, 'Shoulder': 1.95, 'Coat':3.03,
        'Gloves':1.79,'Leggings':2.1, 'Boots': 2.01}

        SalavageRates = [Heavy,Medium,Light]

        if weight == 'Heavy':
                return SalavageRates[0][ArmourType]
        if weight == 'Medium':
                return SalavageRates[1][ArmourType]
        if weight == 'Light' :
                return SalavageRates[2][ArmourType]
        else:
                return 'Error'
        
def RawMaterials(level,weight):
        print(level)
        if weight == 'Heavy':
                if level <20:
                        raw =  19697
                elif 21< level <53 :
                        raw =  19699
                elif  54< level <62:
                        raw = 19702
                elif 63 < level <80:
                        raw = 19684
                return raw
        elif weight == 'Medium':
                if level <18:
                        raw = 19719
                elif 19< level <33 :
                        raw = 19728
                elif 34< level <50:
                        raw = 19730
                elif 51 < level <63:
                        raw = 19731
                elif 64 < level <80:
                        raw = 19729
                return raw
        elif weight == 'Light':
                if level < 18:
                        raw = 19718
                elif 19 < level <33:
                        raw = 19739
                elif 34 < level < 46:
                        raw = 19741
                elif 47 < level < 63:
                        raw = 19743
                elif 64 < level <80:
                        raw = 19748
                return raw




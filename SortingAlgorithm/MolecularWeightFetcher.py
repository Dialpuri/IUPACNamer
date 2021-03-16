import json 
from requests.exceptions import HTTPError
import requests
import time

def request_api(cid):
    try:
        iupac = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'+str(cid)+'/property/IUPACName,MolecularWeight/json').json()
    except HTTPError as http_error:
        return(f'HTTP error occured: {http_error}')
    except Exception as err:
        return(f'Other error has occured: {err}')
    else:
        try: 
            iupac_json = iupac['PropertyTable']['Properties'][0]
        except NameError as name_error:
            print(f'Name error occured: {name_error}')
        except:
            print("An error has occured")
        else:
            return iupac_json

def cid_incremeneter():
    data_to_dump = []
    for cid in range(1,1000):
        json_data = request_api(cid)
        data_to_dump.append(json_data)
        print(cid)
        time.sleep(0.2)
    
    with open('data.txt','w') as data_file:
        json.dump(data_to_dump, data_file)

cid_incremeneter()
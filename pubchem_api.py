import base64
import requests
from requests.exceptions import HTTPError
from cid_selector import cid as cid_selector

def get_data(difficulty):
    cid = cid_selector(difficulty)
    image = get_image_data(cid)
    name = get_iupac(cid)
    return image, name 
    
def get_image_data(cid):
    png = get_png(cid)
    image = bytes_to_base64(png)
    image = 'data:image/png;base64,' + image
    return image

def get_iupac(cid):
    try:
        iupac = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'+str(cid)+'/property/IUPACName/json').json()
    except HTTPError as http_error:
        return(f'HTTP error occured: {http_error}')
    except Exception as err:
        return(f'Other error has occured: {err}')
    else:
        IUPAC_name = iupac['PropertyTable']['Properties'][0]['IUPACName']
        return IUPAC_name

def get_png(cid):
    image_data = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/'+str(cid)+'/PNG')
    return image_data.content

def bytes_to_base64(byte):
    return base64.b64encode(byte).decode('utf-8')


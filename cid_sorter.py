import iupac_checker
import pubchem_api as api
import json 


cid = 1
difficulty = ""

def sorter(): 
    global cid 
    global difficulty
    image, IUPAC_name, cid = api.get_data_DEBUG(cid)
    jsonData = {
        'cid': cid,
        'difficulty': difficulty
    }
    cid = cid + 1

    with open('data.txt', 'a', encoding='utf-8') as json_file: 
        json.dump(jsonData, json_file)

def difficultySorter(difficultyFromServer): 
    global difficulty 
    difficulty = difficultyFromServer
    sorter()

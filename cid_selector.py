import random

cid_index = 0

def cid(difficulty):
    cid_list = get_cid_list(difficulty)
    global cid_index 
    cid_index += 1
    return cid_list[cid_index]

def get_cid_list(fileName):
    try:
        with open(f'{fileName}.txt','r') as cid_file:
                cid_file_read = cid_file.read()
                cid_file_split = cid_file_read.split(' ')
                for i, j in enumerate(cid_file_split):
                    cid_file_split[i] = j.replace(',','')
                return cid_file_split
    except:
        return ['There was an error']

import json

easy = []
medium = []
hard = []
insane = []

with open('data.txt','r') as data_file:
    json_data = json.load(data_file)

    for entry in json_data:
        if entry['MolecularWeight'] <= 150:
            easy.append(entry['CID'])
        elif entry['MolecularWeight'] > 150 and entry['MolecularWeight'] <= 300:
            medium.append(entry['CID'])
        elif entry['MolecularWeight'] > 300 and entry['MolecularWeight'] < 500:
            hard.append(entry['CID'])
        else:
            insane.append(entry['CID'])

with open('easy.txt','w') as easy_file:
    json.dump(easy, easy_file)

with open('medium.txt','w') as medium_file:
    json.dump(medium, medium_file)

with open('hard.txt','w') as hard_file:
    json.dump(hard, hard_file)

with open('insane.txt','w') as insane_file:
    json.dump(insane, insane_file)

print("-----------------------DUMP COMPELETED---------------------------")
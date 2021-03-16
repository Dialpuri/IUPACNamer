import matplotlib.pyplot as plt
import json 

plotData = [[],[]]

with open('data.txt','r') as data_file:
    json = json.load(data_file)

    for entry in json:
        plotData[1].append(entry['MolecularWeight'])
        plotData[0].append(entry['CID'])

plt.scatter(plotData[0],plotData[1])
plt.show()
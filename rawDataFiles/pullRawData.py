import requests as rq 
from bs4 import BeautifulSoup
import textract

res = rq.get('http://minerals.usgs.gov/minerals/pubs/historical-statistics/')
d = res.text 
soup = BeautifulSoup(d, 'lxml')

criticalMinerals = ['quartz', 'cassiterite', 'bauxite', 'bastnaesite', 'copper', 'arsenopyrite', 'silver', 'tantalite', 'wolframite', 'silicon', 'spodumene', 'tungsten', 'tantalum', 'lithium', 'rare earths', 'arsenic', 'aluminum', 'aluminium', 'gallium', 'tin', 'indium']

table = soup.findAll('tbody')
tableSoup = BeautifulSoup(table)
rows = tableSoup.findAll('tr')
linksToExtract = {}
for row in rows:
    temp = BeautifulSoup(str(row))
    try:
        subject = temp.find('a').text
        print ('subject: ' + subject)
        if subject.lower() in criticalMinerals:
            print('Match!!!')
            linkList = []
            links = temp.findAll('a', href = True)  
            for i in links:
                linkList.append(i['href'])
            linksToExtract[subject] = linkList
        else:
            continue
    except AttributeError:
        continue
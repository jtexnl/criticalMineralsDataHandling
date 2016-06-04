'''
This file is used to pull all of the relevant data files on the USGS data page and put them in the directory from which the file is run.
If you want to pull more files, add the names of the minerals for which you want to pull to the 'criticalMinerals' list. 
Be sure that you use the name as it is spelled out on the website.
'''

import requests as rq 
from bs4 import BeautifulSoup
import os
import wget

res = rq.get('http://minerals.usgs.gov/minerals/pubs/historical-statistics/')
d = res.text 
soup = BeautifulSoup(d, 'lxml')

criticalMinerals = ['quartz', 'quartz crystal (industrial)', 'cassiterite', 'bauxite', 'bastnaesite', 'copper', 'arsenopyrite', 'silver', 'tantalite', 'wolframite', 'silicon', 'spodumene', 'tungsten', 'tantalum', 'lithium', 'rare earths', 'arsenic', 'aluminum', 'aluminium', 'gallium', 'tin', 'indium']

table = soup.findAll('tbody')
tableSoup = BeautifulSoup(str(table))
rows = tableSoup.findAll('tr')

linksToExtract = {}

for row in rows:
    temp = BeautifulSoup(str(row))
    try:
        subject = temp.find('a').text
        if subject.lower() in criticalMinerals:
            linkList = []
            links = temp.findAll('a', href = True)  
            for i in links:
                linkList.append(i['href'])
            subjectNew = subject.replace('(', '').replace(')', '')
            linksToExtract[subjectNew] = linkList
        else:
            continue
    except AttributeError:
        continue

def pullFile (link):
    baseURL = 'http://minerals.usgs.gov/minerals/pubs/historical-statistics/'
    wget.download(baseURL + link)

os.mkdir('Tin')

for key, value in linksToExtract.items():
    if not key in os.getcwd():
        os.mkdir(key.replace(' ', '_'))
        os.chdir(key.replace(' ', '_'))
        files = linksToExtract[key]
        for i in files:
            pullFile(i)
        os.chdir('..')
    else:
        os.chdir(key.replace(' ', '_'))
        files = linksToExtract[key]
        for i in files:
            pullFile(i)
        os.chdir('..')
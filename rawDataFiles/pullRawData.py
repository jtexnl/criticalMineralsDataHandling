import requests as rq 
from bs4 import BeautifulSoup
import textract

res = rq.get('http://minerals.usgs.gov/minerals/pubs/historical-statistics/')
d = res.text 
soup = BeautifulSoup(d, 'lxml')

table = soup.findAll('tbody')

criticalMinerals = ['quartz', 'cassiterite', 'bauxite', 'bastnaesite', 'copper', 'arsenopyrite', 'silver', 'tantalite', 'wolframite', 'silicon', 'spodumene']


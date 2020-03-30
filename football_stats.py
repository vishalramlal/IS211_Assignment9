#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 9 Part 1


import urllib.request
import sys
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")


find_table = soup.find_all('table', {'class': 'data'})

for i in find_table:
    table = i


tRows = table.find_all('tr', {'class': lambda L: L and L.startswith('row')})


alldata = []


for i in tRows:
    if (len(alldata)) < 20:
        tData = i.find_all('td')
        name = str(tData[0].get_text())
        ppos = str(tData[1].get_text())
        pteam = str(tData[2].get_text())
        tdown = str(tData[6].get_text())
        alldata.append('Player:{}, Position:{}, Team:{}, Touchdowns:{}'.format(name, ppos, pteam, tdown))
        print('Player:{}, Position:{}, Team:{}, Touchdowns:{}'.format(name, ppos, pteam, tdown))
    else:
        break





# In[ ]:





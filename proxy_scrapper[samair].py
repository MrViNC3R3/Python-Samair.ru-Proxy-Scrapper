import requests
from bs4 import BeautifulSoup
import time

#URL's
URL = []
for a in range(1,21):
    if a <= 9:
        URL.append('http://samair.ru/proxy/proxy' + '-' + '0' + str(a) + '.htm')

    else:
        URL.append('http://samair.ru/proxy/proxy' + '-' + str(a) + '.htm')


for u in URL:
    print 'Scrapping From ' + u

    r = requests.get(u)
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
#making File
    f = open('proxy.txt','a')

    table = soup.find_all('tr',attrs = {'class':'anon'})
    if table > 0:
        for t in table:
            for d in t.find('td'):
                f.write(d + '\n')


    table = soup.find_all('tr',attrs = {'class':'elite'})
    if table > 0:
        for t in table:
            for d in t.find('td'):
                f.write(d + '\n')


    table = soup.find_all('tr',attrs = {'class':'trans'})
    if table > 0:
        for t in table:
            for d in t.find('td'):
                f.write(d + '\n')
    time.sleep(1)
    f.close()

print 'Scrapped in proxy.txt'

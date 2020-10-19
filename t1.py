from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import requests
import json
import csv
import random

csv_file = open('csv_jobs.csv', 'a')
writer = csv.DictWriter(csv_file, ['id', 'Title', 'Data', 'Empresa','Faixa salarial','Estado','Local da vaga','Nível','Aceita Remoto?','Tipo de contratação'])
writer.writeheader()

url = 'https://www.pyjobs.com.br/job/{}/'

# PAGES
for i in range(1000,1500):

    info = {}

    # number = random.randint(1000,2000)
    # response = requests.get(url.format(number))
    response = requests.get(url.format(i))
    soup = BeautifulSoup(response.content, 'html.parser')
    
    try:
        info['id'] = i #number
        info['Title'] = soup.find('h2').get_text()
        info['Data'] = soup.find('h3').get_text().split(':')[1].strip()
    except Exception:
        continue

    for i in soup.findAll('li'):
        if i == None: continue
        
        itext = i.get_text()

        if 'Empresa' in itext: info['Empresa'] = i.get_text().split(':')[1].strip()
        if 'Faixa salarial' in itext: info['Faixa salarial'] = i.get_text().split(':')[1].strip()
        if 'Estado' in itext: info['Estado'] = i.get_text().split(':')[1].strip()
        if 'Local da vaga' in itext: info['Local da vaga'] = i.get_text().split(':')[1].strip()
        if 'Nível' in itext: info['Nível'] = i.get_text().split(':')[1].strip()
        if 'Aceita Remoto?' in itext: info['Aceita Remoto?'] = i.get_text().split(':')[1].strip()
        if 'Tipo de contratação' in itext: info['Tipo de contratação'] = i.get_text().split(':')[1].strip()

    print(json.dumps(info, indent=4))
    # writer.writerow(info)

csv_file.close()

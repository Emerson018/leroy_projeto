import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests
import re
import random

def requisition(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    req = requests.get(url,headers=headers)
    html_content = req.text
    soup = BeautifulSoup(html_content,"html.parser")

    return soup


def find_price(prod_price):

    linhas_texto = []

    # Write_archive__
    buffer = StringIO()
    writer = csv.writer(buffer)
    writer.writerows(prod_price)

    buffer.seek(0)
    reader = csv.reader(buffer)

    for row in reader:
        linhas_texto.append('.'.join(row))

    return '\n'.join(linhas_texto)

url2 = 'https://www.google.com.br/search?q='

def random_int():
    return random.randint(1, 40)

def random_float():
    return round(random.uniform(2.0,4.8),1)

# raiting__
def get_review(lm):

    concat_url = url2 + lm + '+leroy+merlin'
    get_info = requisition(concat_url).find('div', class_='fG8Fp uo4vr').text

    avalia = re.search(r'Avaliação: (\d,\d+)', get_info)
    comentario = re.search(r'(\d+) comentários', get_info)
    if avalia:
        media_avaliacao = avalia.group(1).replace(',',('.'))
        avaliacao = comentario.group(1)
        return int(avaliacao), float(media_avaliacao)
    else:
        print('Não há avaliações para esse produto')
        media_avaliacao = random_int()
        avaliacao = random_float()
        return media_avaliacao, avaliacao
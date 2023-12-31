import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests
import re
import random
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile



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
        media_avaliacao = random_int()
        avaliacao = random_float()
        return media_avaliacao, avaliacao
    
def get_image(url):
    img_tag = requisition(url).find('img')

    img_url = img_tag['src']
    img_data = requests.get(img_url).content
    
    img_filename = img_url.split("/")[-1]

    img_content = ContentFile(img_data)
    img_path = default_storage.save(img_filename,img_content)
    
    return img_path

def get_title_and_lm(url,title_element):
    title = title_element.text.replace('\n', '').replace('&','e').replace('+', ' plus')
    html_code = requisition(url).find('div', class_='badge product-code badge-product-code').text
    lm = ''
    for caractere in html_code:
        if caractere.isdigit():
            lm += caractere

    return title, lm 

def get_info_produto(url):
    info_produto = requisition(url).find('table', class_='characteristics-table')
    dict_produto = {}
    for linha in info_produto.find_all('tr'):
        chave = linha.th.text.strip()
        valor = linha.td.text.strip()
        dict_produto[chave] = valor

    return dict_produto
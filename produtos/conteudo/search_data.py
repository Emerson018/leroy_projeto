import csv
from io import StringIO

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

def data_get(soup):

    title_element = soup.find('h1', class_='product-title align-left color-text')
                
    if title_element:
        title = title_element.text.replace('\n', '')
        barcode = soup.find('div', class_='badge product-code badge-product-code').text
        lm = ''
        for caractere in barcode:
            if caractere.isdigit():
                lm += caractere

        prod_price = soup.find('div',class_='product-price-tag')


    return title, prod_price, lm

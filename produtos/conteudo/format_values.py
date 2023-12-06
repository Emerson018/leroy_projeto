import re

def format_real(text_lines):

    default = r"data-price='{\s*\"integers\"\s*:\s*\"([\d.]+)\"\s*,\s*\"decimals\"\s*:\s*\"([\d]+)\"\s*}'"
    matches = re.search(default, text_lines)
    if matches:
        integers, decimals = matches.groups()
        price = f"{integers.replace('.','')}.{decimals}"
    return price

def format_data(reais, centavos, ean_13, title):
    # format_price__
    preco = (reais + centavos)

    # format_data__
    product = {'LM': [int(ean_13)],
               'Title': [str(title)],
               'Price': [float(preco)]}
    produtos_csv = [ean_13, title, preco]

    return product, produtos_csv, preco

def format_info(infos):
    if infos is not None:
        informacao = infos.find_next('td').text
    else:
        informacao = '---'

    return print(informacao)
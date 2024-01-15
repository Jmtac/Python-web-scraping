import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://lista.mercadolivre.com.br/'
nome = str(input('nome do produto: ')).replace(' ', '-')
url = url_base + nome

response = requests.get(url)

content = response.content

site = BeautifulSoup(content, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat '
                                               'andes-card--padding-16'})
products_list = []

for produto in produtos:
    nome = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    reais = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos = produto.find('span',
                            attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})
    if centavos:
        preco = f'R${reais.text},{centavos.text}'
    else:
        preco = f'R${reais.text},00'
    link = produto.find('a',
                        attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    products_list.append([nome.text, preco, link['href']])

products = pd.DataFrame(products_list, columns=['nome', 'preço', 'link'])
print(products)

products.to_excel('produtos.xlsx', index=False)

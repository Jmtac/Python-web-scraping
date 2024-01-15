import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

news = site.findAll('div', attrs={'class': 'feed-post-body'})

news_list = []

for new in news:
    titulo = new.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    subtitilo = new.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
    if subtitilo:
        news_list.append([titulo.text, subtitilo.text, titulo['href']])
    else:
        news_list.append([titulo.text, '', titulo['href']])

noticia = pd.DataFrame(news_list, columns=['titulo', 'subtitulo', 'link'])

noticia.to_excel('news.xlsx', index=False)

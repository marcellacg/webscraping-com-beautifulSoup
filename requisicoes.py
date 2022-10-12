import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser') #conteudo vira objeto do beautifulSoup para buscar tags
# noticia = site.find('div', attrs={'class': 'feed-post-body'})#html da noticia
# titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})#procurar o titulo dentro dela
# print(titulo.text)
# #subtitulo
# #print(noticia.prettify())
# subtitulo = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
# print(subtitulo.text)

#AGORA COM TODAS AS NOTICIAS
noticias = site.findAll('div', attrs={'class': 'feed-post-body'}) #aqui já é um set do beautifulsoup, logo, uma lista
for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    #print(titulo.text)
    #print(titulo['href']) #link da noticia
    #print(noticia.prettify())
    #subtitulo
    subtitulo = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
    #pra verificar se o subtitulo existe
    if (subtitulo):
        print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']]) #lista de listas, pois é para cada noticia
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])
news.to_excel('noticias.xlsx', index=False)
from math import prod
from urllib import response
import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'
produto_item = input("Digite o produto: ")
resposta = requests.get(url_base + produto_item)
site = BeautifulSoup(resposta.text, 'html.parser')
# produto = site.find('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})#esse produto é o que tem todas as infos do produto
# titulo = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'}) #deriva de produto
# link = produto.find('a', attrs={'class': 'ui-search-link'}) #deriva de produto
# #print(link['href'])#acesso como dicionario
# #print(titulo.text)
# reais = produto.find('span', attrs={'class': 'price-tag-fraction'})
# cifrao = produto.find('span', attrs={'class': 'price-tag-symbol'})
# print('Preço do produto: ', cifrao.text, reais.text)

#PARA MAIS PRODUTOS:

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})#esse produto é o que tem todas as infos do produto
for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'}) #deriva de produto
    link = produto.find('a', attrs={'class': 'ui-search-link'}) #deriva de produto
    #print(link['href'])#acesso como dicionario
    #print(titulo.text)
    reais = produto.find('span', attrs={'class': 'price-tag-fraction'})
    cifrao = produto.find('span', attrs={'class': 'price-tag-symbol'})
    cents = produto.find('span', attrs={'class': 'prince-tag-cents'})

    print('Nome do produto: ', titulo.text)
    print('Link do produto: ', link['href'])

    if (cents):
        print('Preço do produto: ', cifrao.text, reais.text, cents.text)
    else:
        print('Preço do produto: ', cifrao.text, reais.text)

    print('\n\n')
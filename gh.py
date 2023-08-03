from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from sys import argv as argumentos
from sys import exit as sair

# Creator/Criador: DTBrowser
# Versão/Version: 1.0

def get_links(dork, limite):
    files = []
    SEARCH = f"https://www.google.com/search?q={dork}&limit={int(limite)}"
    chrome = webdriver.Chrome()
    chrome.get(SEARCH)
    html = chrome.page_source
    html = BeautifulSoup(html, 'html.parser')
    divs = html.findAll('div', attrs={'class': 'yuRUbf'})
    for div in divs:
        for links in div.findAll('a'):
            f = links['href']
            files.append(f)
    chrome.close()
    return files

def preparar_files(lista):

    lista_dict = []
    for i in lista:
        dicionario = {}
        link = i
        nome = i.split('/')[-1]
        dicionario.update({nome:link})
        lista_dict.append(dicionario)
    return lista_dict

def download_files(lista_dict):
    for i in lista_dict:
        for i1, (nome, link) in enumerate(i.items()):
            r = requests.get(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})
            f = open(nome, 'wb')
            f.write(r.content)
            f.close()

def preparar_dork(dork_inicial):
    dork = dork_inicial.replace(' ','+')
    return dork

def main():
    try:
        dork_inicial = argumentos[1]
        print(dork_inicial)
    except:
        print("Uso: python3 gh.py <dork>")
        sair()
    dork = preparar_dork(dork_inicial)
    lista = get_links(dork, 10)
    lista_dict = preparar_files(lista)
    download_files(lista_dict)

if __name__ == '__main__':
    main()






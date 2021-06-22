#/*---- Teste 1 - WebScraping -----
   
# Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute 
# as tarefas de código abaixo.
# Tarefas de código:
#     - 1.1 - Acessar o site: http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar;
#     - 1.2 - Buscar a versão mais recente do Padrão TISS (arquivo - padrao_tiss_componente_organizacional_[data].pdf);
#     - 1.3 - Baixar o componente organizacional;*/

####################################################################################################################

from bs4 import BeautifulSoup
import requests
import re 

html = requests.get("https://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar").content

soup = BeautifulSoup(html,'html.parser')

elementoA = soup.find("a", class_='alert-link')

linkPadraoTiss = "https://www.ans.gov.br" + elementoA.get('href')

print(" ")
print("Acessando URL Padrao Tiss: " + linkPadraoTiss)
print(" ")

#####################################################################################################################

html = requests.get(linkPadraoTiss).content

soup = BeautifulSoup(html, 'html.parser')

elementoDownloadPDF = soup.findAll('a', href=re.compile("pdf"), attrs={'class':'btn btn-primary btn-sm center-block'})

linkDownloadPDF = 'https://www.ans.gov.br' + elementoDownloadPDF[0].get('href')

print(" ")
print("Acessando URL download PDF Padrao Tiss: " + linkDownloadPDF)
print(" ")

######################################################################################################################

resposta = requests.get(linkDownloadPDF)

nomeDoArquivo = 'teste.pdf'

with open(nomeDoArquivo, 'wb') as f:
    f.write(resposta.content)

print(" ")
print('Pdf slavo com sucesso!')
print(" ")

#######################################################################################################################
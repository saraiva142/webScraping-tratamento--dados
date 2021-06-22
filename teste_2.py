#---- Teste 2 Transformação de dados -----

# Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute 
# as tarefas de código abaixo.
# Tarefas de código:
#     - Extrair do pdf do teste 1 acima os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS);
#     - Salvar dados dessas tabelas em csvs;
#     - Zipar todos os csvs num arquivo "Teste_Intuitive_Care_{seu_nome}.zip".

######################################################################################################################

import tabula
from zipfile import ZipFile

file = "teste.pdf"

tables = tabula.read_pdf(file, pages = "79-85", multiple_tables = True)

print('Extraindo tabelas')

tables[0].to_csv('tabela30.csv', encoding='utf-8')
tables[1].to_csv('tabela31.csv', encoding='utf-8')
tables[2].to_csv('tabela32.csv', encoding='utf-8')

print('Extração concluida')

#######################################################################################################################

print('Zipando arquivos')

zipObj = ZipFile('Teste_Intuitive_Care_Joao_Victor.zip', 'w')
zipObj.write('tabela30.csv')
zipObj.write('tabela31.csv')
zipObj.write('tabela32.csv')
zipObj.close()

print('Processando concluido')
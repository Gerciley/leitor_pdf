#Importando as bibliotecas
from logging import exception
from rarfile import RarFile
import os

#Nome do arquivo, deve-se renomar para o nome do arquivo .rar
arquivo_rar = '/content/NFS 04.09 A 10.09.rar'

#Abre o arquivo .rar
with RarFile(arquivo_rar) as nota_desc:

  try:
    #Efetua a extração do arquivo
    nota_desc.extractall('/content/fonte')

    #Lista os arquivos extraídos
    extraidos = os.listdir('/content/fonte')

    print(f'Foram extraídos {len(extraidos)} de um total de {len(nota_desc.infolist())}')
  except Exception as e:
    print('Ocorreu um erro ao extrair os arquivos!')
    print (e)


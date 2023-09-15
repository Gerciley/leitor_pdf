#importando as blibliotecas
import pdfplumber
import os
import pandas as pd
from datetime import datetime

#Matriz vazia que receberá os dados de interesse
matrix = {
    'CNPJ Loja': [],
    'Data Emissão' : [],
    'Numero NF Referência' : [],
    'Número NF' : [],
    'Valor' : []
}

#lendo os arquivos
file_list = os.listdir('/content/fonte')
lista_pdf = [arquivo for arquivo in file_list if arquivo.lower().endswith('pdf')]
status = 'SUCESSO'

for i, arquivo in enumerate(lista_pdf):
  try:
    with pdfplumber.open(f'/content/fonte/{arquivo}') as pdf_file:
      pagina = pdf_file.pages[0]
      conteudo = pagina.extract_text_lines()

  except Exception as e:
    print(e)
    status = 'ERRO'
    processo = i+1
    arquivo_erro = arquivo

  finally:

    #Atribuindo os valores as suas respectivas variáveis
    numero_nf_ref = str(conteudo[24]['text']).split()[3]
    numero_nf=  str(conteudo[4]['text']).split()[1]
    data_emissao = str(conteudo[4]['text']).split()[2]
    cnpj_suporte = str(conteudo[20]['text']).split()
    cnpj_loja = str(cnpj_suporte[0]).split(':')[1]
    valor_nf = str(conteudo[24]['text']).split()[-1]

    #criando a matriz de dados
    matrix['CNPJ Loja'].append(cnpj_loja)
    matrix['Numero NF Referência'].append(numero_nf_ref)
    matrix['Número NF'].append(numero_nf)
    matrix['Data Emissão'].append(data_emissao)
    matrix['Valor'].append(valor_nf)

    print(f'Processo: {i+1}/{len(file_list)}: {arquivo}')


#Criando o dataframe
matrix_df = pd.DataFrame(matrix)

#Exportando dataframe para csv
date = datetime.now()
matrix_df.to_csv(f'info_from_pdf - {date}.csv', sep= ';', encoding='utf-8', header=True, index=False)

print('#'*100)
print(f'FINALIZADO COM {status}')
if status == 'ERRO':
  print(f'Erro no processo: {processo}')
  print(f'arquivo: {arquivo}')

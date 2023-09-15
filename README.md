# leitor_pdf
Uso da Biblioteca pdfplumber para ler arquivos PDF (Notas Fiscais) extrair alguns dados e Salvar em um arquivo csv

# Extrator de Dados de Notas Fiscais de Serviço

O Extrator de Dados de Notas Fiscais de Serviço é uma ferramenta desenvolvida em Python que permite extrair informações de Notas Fiscais de Serviço em formato PDF. Ele é projetado para lidar com notas fiscais que seguem um padrão específico e são enviadas em arquivos compactados no formato RAR.


## Funcionalidades

- Descompacta arquivos RAR contendo várias Notas Fiscais de Serviço em formato PDF.
- Extrai informações específicas das Notas Fiscais, como número, data, valor, etc.
- Armazena os dados extraídos em uma matriz.
- Exporta os dados para um arquivo CSV para análise posterior.

## Pré-requisitos

Antes de usar o Extrator de Dados, certifique-se de ter instalado os seguintes pré-requisitos:

- Python 3.x
- Bibliotecas Python (listadas no arquivo `requirements.txt`, você pode instalá-las usando `pip`)

## Instalação

Contribuição
Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga os passos:

Faça um fork deste repositório.
Crie uma branch com sua feature ou correção de bug: git checkout -b minha-feature
Faça commit das mudanças: git commit -m 'Adicione uma nova feature'
Envie suas alterações: git push origin minha-feature
Abra um Pull Request.

Contato
Para entrar em contato com a equipe do projeto, envie um e-mail para [gerciley.fa@gmail.com].

Status do Projeto
Projeto inicial já em uso em linha de comando e executado no Google Colab ou diretamente da IDE de desenvolvimetno,
projeto foi pensado em ateder uma necessidade pontual, contudo o projeto será estruturado para receber uma interface gráfica e oferecer mais opções, como por exemplo mostrar uma página
e oferecer a opção do usuário selecionar e escolher quais dados deseja extrair.

============================================================================================================================================================================================================
pdf_reader
Using the pdfplumber Library to Read PDF Files (Invoices), Extract Data, and Save it to a CSV File

Invoice Data Extractor
The Invoice Data Extractor is a Python tool that allows you to extract information from PDF-format Service Invoices. It is designed to handle invoices that follow a specific pattern and are sent in RAR-compressed files.

Features
Unpack RAR files containing multiple PDF-format Service Invoices.
Extract specific information from the invoices, such as invoice number, date, amount, etc.
Store the extracted data in an array.
Export the data to a CSV file for further analysis.
Prerequisites
Before using the Invoice Data Extractor, make sure you have installed the following prerequisites:

Python 3.x
Python libraries (listed in the requirements.txt file; you can install them using pip)
Installation
Contribution
Contributions are welcome! If you want to contribute to the project, follow these steps:

Fork this repository.
Create a branch for your feature or bug fix: git checkout -b my-feature
Commit your changes: git commit -m 'Add a new feature'
Push your changes: git push origin my-feature
Open a Pull Request.
Contact
To get in touch with the project team, send an email to [gerciley.fa@gmail.com].

Project Status
The initial project is already in use via the command line and can be run in Google Colab or directly from the development IDE. The project was initially designed to meet a specific need, but it will be structured to include a graphical interface and offer more options, such as displaying a page and allowing the user to select and choose which data to extract.

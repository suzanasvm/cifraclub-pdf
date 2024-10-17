# Cifra Club PDF Generator

Este projeto em Python é uma ferramenta que busca cifras de músicas no formato de impressão do site Cifra Club e as gera em um PDF organizado em duas colunas. Utilizando as bibliotecas `requests`, `BeautifulSoup` e `FPDF`, o programa permite a coleta de cifras de forma simples e prática, sem tablaturas.

## Funcionalidades

- **Busca de Cifras**: Localiza a cifra da música desejada com base no nome do cantor e da música, formatando a URL de acordo com o padrão do Cifra Club.
- **Remoção de Tablaturas**: Filtra as linhas de tablatura para apresentar apenas as cifras.
- **Geração de PDF**: Cria um PDF que organiza as cifras em duas colunas, facilitando a leitura e impressão.
- **Leitura de Arquivo**: Permite a entrada de múltiplas músicas e cantores a partir de um arquivo de texto.

## Como Usar

1. Instale as bibliotecas necessárias:
   pip install requests beautifulsoup4 fpdf
   
2. Crie um arquivo de texto (musicas.txt) com a lista de músicas e cantores, cada linha no formato: música,cantor.
3. Execute o script:
  python cifra_club_pdf_generator.py

Um arquivo PDF chamado cifras.pdf será gerado, contendo as cifras formatadas.

## Exemplo de uso (Arquivo musicas.txt)
Exagerado, Cazuza
<br> Insira o nome da musica e em seguida uma virgula com o nome do cantor

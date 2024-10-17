import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import re
#Implementado por Suzana Mota
def buscar_cifra(musica, cantor):
    musica_formatada = musica.lower().replace(' ', '-')
    cantor_formatado = cantor.lower().replace(' ', '-')
    url_cifra = f"https://www.cifraclub.com.br/{cantor_formatado}/{musica_formatada}/imprimir.html#key=8&columns=true&footerChords=false&tabs=false&font=16"
    response = requests.get(url_cifra)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        cifra_html = soup.find('pre')
        
        if cifra_html:
            cifra = cifra_html.text
            cifra_sem_tablatura = remover_tablatura(cifra)
            return cifra_sem_tablatura
        else:
            return "Cifra não encontrada."
    else:
        return f"Cifra não encontrada para {musica} de {cantor}."

def remover_tablatura(cifra):
    padrao_tablatura = re.compile(r"^[EADGB]\|.*\|.*$")
    linhas = cifra.split('\n')
    linhas_sem_tablatura = [linha for linha in linhas if not padrao_tablatura.match(linha)]
    return '\n'.join(linhas_sem_tablatura)

def gerar_pdf(nomes_musicas, cifras):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    largura_coluna = pdf.w / 2
    altura_linha = 6

    for i, (musica, cantor) in enumerate(nomes_musicas):
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"{musica} - {cantor}", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        x_coluna1 = 10
        x_coluna2 = largura_coluna + 10
        linhas = cifras[i].split('\n')
        current_y = 20
        column_one_full = False
        column_two_full = False

        for linha in linhas:
            if not column_one_full:
                pdf.set_xy(x_coluna1, current_y)
                pdf.multi_cell(largura_coluna - 20, altura_linha, linha)
                current_y = pdf.get_y()

                if current_y > pdf.h - 20:
                    current_y = 20
                    pdf.set_xy(x_coluna2, current_y)
                    column_one_full = True

            elif not column_two_full:
                pdf.set_xy(x_coluna2, current_y)
                pdf.multi_cell(largura_coluna - 20, altura_linha, linha)
                current_y = pdf.get_y()

                if current_y > pdf.h - 20:
                    pdf.add_page()
                    pdf.set_font("Arial", 'B', 16)
                    pdf.cell(0, 10, f"{musica} - {cantor} (cont.)", ln=True, align='C')
                    pdf.ln(10)
                    pdf.set_font("Arial", size=12)
                    current_y = 20
                    pdf.set_xy(x_coluna1, current_y)
                    column_one_full = False
                    column_two_full = False
                    continue

        if column_one_full and column_two_full:
            continue

    pdf.output("cifras.pdf")

def main(arquivo_txt):
    with open(arquivo_txt, 'r') as file:
        nomes_musicas = [linha.strip().split(',') for linha in file.readlines()]
    
    cifras = []
    for musica, cantor in nomes_musicas:
        print(f"Buscando cifra para: {musica} de {cantor}")
        cifra = buscar_cifra(musica.strip(), cantor.strip())
        cifras.append(cifra)
        print(f"Cifra encontrada para {musica} de {cantor}.\n")

    print("Gerando PDF em duas colunas...")
    gerar_pdf(nomes_musicas, cifras)
    print("PDF gerado com sucesso: cifras.pdf")

if __name__ == "__main__":
    arquivo_txt = "musicas.txt"
    main(arquivo_txt)

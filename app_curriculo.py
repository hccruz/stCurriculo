from pathlib import Path
import streamlit as st
from PIL import Image

# Configurações Estruturais

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "main.css"
arquivo_pdf = diretorio / "assets" / "Curriculo_CD.pdf"
arquivo_img = diretorio / "assets" / "heraldo01.jpg"

# Configurações Gerais das Informações

TITULO = "Currículo | Heraldo Candido da Cruz"
NOME = "Heraldo Candido da Cruz"
DESCRICAO = """
    Sou formando em Matemática com Informática e cursando Bacharel com Ciências
    de Dados no último semestre e atualmente trabalho como programador de VBA e
    Python no mercado de vendas de produtos hospitalares.

    Apaixonado por Ciências de Dados, com certificação em Python e linguagem R,
    ofereço conhecimentos em análise de dados e programação de computadores.
    Sou colaborativo, flexível e capaz de trabalhar sob pressão e atingir os
    objetivos nos prazos estabelecidos. Sou também muito comunicativo, gosto de
    trabalhar em equipe e sou bem-organizado.

    Estou buscando uma oportunidade de trabalhar profissionalmente como
    Cientista ou Analista de Dados para melhorar a tomada de decisão da
    empresa, através da construção de soluções usando dados.
"""
TELEFONE = "(011)99662-8133"
EMAIL = "hccruz@gmail.com"
MIDIA_SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/heraldocruz/",
    "GitHub": "https://github.com/hccruz"
}

# CURSOS = {
#     "🎯 "
# }

st.set_page_config(page_title=TITULO)

# Carregando Assets

with open(arquivo_css) as c:
    st.markdown(f"<style>{c.read()}</style>", unsafe_allow_html=True)

with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()

imagem = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(imagem, width=250)

with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label="Download Currículo",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write("✉️", EMAIL)

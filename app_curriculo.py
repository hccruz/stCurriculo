from pathlib import Path
import streamlit as st
from PIL import Image

# Configurações Estruturais

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "main.css"
arquivo_pdf = diretorio / "assets" / "Curriculo_CD.pdf"
arquivo_img = diretorio / "assets" / "heraldo.jpg"


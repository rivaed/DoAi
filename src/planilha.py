
import gspread
import streamlit as st
import json
from google.oauth2.service_account import Credentials

# Carrega os dados do segredo como dicionário
service_account_info = json.loads(st.secrets["GOOGLE_CREDENTIALS_JSON"])

# Define os escopos necessários
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Constrói as credenciais
creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

# ID da planilha (vindo dos secrets)
GOOGLE_SHEET_ID = st.secrets["GOOGLE_SHEET_ID"]

def conectar_planilha():
    client = gspread.authorize(creds)
    sheet = client.open_by_key(GOOGLE_SHEET_ID)
    return sheet

def registrar_entrada(alimento, quantidade, origem):
    sheet = conectar_planilha()
    aba = sheet.worksheet("Entradas")
    nova_linha = [alimento, quantidade, origem]
    aba.append_row(nova_linha)
    print(f"Registrado: {quantidade} de {alimento}")

def registrar_saida(alimento, quantidade, grupo):
    sheet = conectar_planilha()
    aba = sheet.worksheet("Saídas")
    nova_linha = [alimento, quantidade, grupo]
    aba.append_row(nova_linha)
    print(f"Distribuído: {quantidade} de {alimento} para {grupo}")

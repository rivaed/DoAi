
import os
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

# Caminho para as credenciais e ID da planilha
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_PATH")

# Escopos necessários
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

def conectar_planilha():
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(GOOGLE_SHEET_ID)
    return sheet

def registrar_entrada(alimento, quantidade, origem="Doação direta"):
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

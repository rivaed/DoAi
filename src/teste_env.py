from dotenv import load_dotenv
import os

load_dotenv()

print("SHEET ID:", os.getenv("GOOGLE_SHEET_ID"))
print("Credenciais:", os.getenv("GOOGLE_CREDENTIALS_PATH"))

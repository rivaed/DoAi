import streamlit as st
from src.planilha import registrar_entrada, registrar_saida

st.set_page_config(page_title="DoAí - Registro de Doações", layout="centered")

st.title("DoAí - Registro de Doações")

modo = st.radio("O que você quer registrar?", ["Entrada", "Saída"], horizontal=True)

# Lista de alimentos comuns
alimentos_comuns = [
    "Arroz", "Feijão", "Melancia", "Macarrão", "Farinha", "Açúcar", "Sal", "Óleo", "Leite",
    "Café", "Milho", "Batata", "Cenoura", "Abóbora", "Repolho", "Tomate", "Alface", "Pão"
]

with st.form("registro_form"):
    alimento = st.selectbox("Alimento", alimentos_comuns)
    quantidade = st.selectbox("Quantidade (kg)", list(range(1, 51)))
    
    if modo == "Entrada":
        origem = st.text_input("Origem da doação", placeholder="Ex: Feira, Doação direta")
    else:
        grupo = st.text_input("Grupo destinatário", placeholder="Ex: Grupo A, Grupo B")
    
    observacoes = st.text_area("Observações (opcional)", placeholder="Algum detalhe adicional?")

    enviado = st.form_submit_button("Registrar")

    if enviado:
        if modo == "Entrada":
            if not origem.strip():
                st.error("Informe a origem da doação.")
            else:
                registrar_entrada(alimento, f"{quantidade}kg", origem, observacoes)
                st.success(f"{quantidade}kg de {alimento} registrado como entrada.")
        else:
            if not grupo.strip():
                st.error("Informe o grupo destinatário.")
            else:
                registrar_saida(alimento, f"{quantidade}kg", grupo, observacoes)
                st.success(f"{quantidade}kg de {alimento} registrado como saída.")

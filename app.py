import streamlit as st
from src.planilha import registrar_entrada, registrar_saida

# Configurações da página
st.set_page_config(page_title="DoAí - Registro de Doações", layout="centered")

# Usuários e senhas
USUARIOS = {
    "flor": "123",
    "edu": "123",
    "entregador": "123"
}

# Inicializa sessão
if "usuario_autenticado" not in st.session_state:
    st.session_state.usuario_autenticado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# Tela de login
def exibir_login():
    st.title("DoAí - Acesso Restrito")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state.usuario_autenticado = True
            st.session_state.usuario = usuario
            st.success("Login realizado com sucesso.")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos.")

# Tela principal após login
def exibir_app():
    usuario = st.session_state.usuario
    st.title(f"DoAí - Registro de Doações ({usuario})")

    if usuario == "entregador":
        modo = "Saída"
        st.info("Você está no modo restrito: apenas registros de SAÍDAS estão disponíveis.")
    else:
        modo = st.radio("O que você quer registrar?", ["Entrada", "Saída"], horizontal=True)

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

    # Botão de logout
    if st.button("Sair"):
        st.session_state.usuario_autenticado = False
        st.session_state.usuario = ""
        st.experimental_rerun()

# Fluxo principal
if not st.session_state.usuario_autenticado:
    exibir_login()
else:
    exibir_app()

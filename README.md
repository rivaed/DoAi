
# DoAí

**Sistema Inteligente de Registro de Doações de Alimentos**

DoAí é uma interface web integrada ao Dify (LangChain) que permite o registro automatizado de **entradas** e **saídas** de doações de alimentos. Tudo é armazenado em uma planilha e organizado de forma a facilitar análises futuras via dashboards.

## ⚙️ Funcionalidades

- Registro via linguagem natural (ex: “Recebemos 20kg de melancia e 10kg de arroz”)
- Separação de registros por **entrada** e **distribuição**
- Integração com planilhas (Google Sheets ou compatível)
- Suporte à organização de doações por **grupos familiares**
- Base para construção de painéis e indicadores em Power BI ou Data Studio

## 🔁 Fluxo de uso

1. **Recebimento**  
   O operador informa o que foi doado. Exemplo:  
   > "Recebemos 10kg de cenoura e 5kg de batata."

2. **Distribuição**  
   Outro operador registra a entrega para grupos. Exemplo:  
   > "Distribuímos 5kg de cenoura para o Grupo A e 5kg para o Grupo B."

3. **Planilha Atualizada**  
   As entradas e saídas são registradas automaticamente.

## 🧠 Tecnologias

- [Dify](https://dify.ai/) com LangChain
- Planilha como backend (Google Sheets)
- Automação com Python ou Node.js (dependendo do integrador)
- Integração futura com BI

## 📁 Estrutura do Projeto

```
DoAi/
├── src/               # Código principal de integração
├── docs/              # Documentação e design
├── tests/             # Testes automatizados
├── .gitignore
├── README.md
└── LICENSE
```

## 📌 Requisitos

- Conta ativa no [Dify](https://dify.ai/)
- API Key e credenciais de acesso à planilha
- Python 3.9+ (caso use scripts Python)
- Autorização para uso do projeto

## 📄 Licença

Este projeto é **proprietário** e **não possui licença open source**.

Todos os direitos reservados © BeeAi42, 2025.  
O uso, redistribuição ou modificação deste software **sem autorização expressa por escrito** do autor é **estritamente proibido**.

Para solicitar permissão ou colaboração, entre em contato.

---

> **DoAí** nasceu para simplificar a solidariedade com tecnologia. E aqui, inteligência artificial trabalha por um mundo mais justo – mas só com minha autorização, claro.

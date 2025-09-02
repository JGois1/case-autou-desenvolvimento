# Classificador de Emails - Case Prático AutoU

Este projeto foi desenvolvido para o case prático da AutoU. É uma aplicação web que usa IA para classificar emails como "Produtivo" ou "Improdutivo" e sugerir uma resposta.

## Tecnologias

-   **Backend:** Python com Flask
-   **Frontend:** HTML e CSS básico
-   **IA:** API do Google AI (Modelo Gemini)

## Como Rodar o Projeto

**1. Clone o repositório:**
```bash
git clone [https://github.com/JGois1/case-autou-desenvolvimento.git](https://github.com/JGois1/case-autou-desenvolvimento.git)
cd case-autou-desenvolvimento
```

**2. Crie e ative um ambiente virtual:**
```bash
python -m venv venv

.\venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```
> **Aviso:** Certifique-se de ter um arquivo `.env` na raiz do projeto com sua `GOOGLE_API_KEY` para que a aplicação funcione.

**4. Rode a aplicação:**
```bash
flask run
```

Depois, é só abrir o navegador e acessar `http://127.0.0.1:5000`.

## Links do Projeto

-   **Aplicação Online:** https://case-autou-joaogois.onrender.com
-   **Vídeo de Demonstração:** https://youtu.be/Psf-gc1t7J0

## Obs: Se não abrir de primeira o link do Render aguarde 1 minuto e dê F5 para o servidor 'acordar', obrigado!

---
**Desenvolvido por:** João Gois de Otoni

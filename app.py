import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    
    raise ValueError("A chave GOOGLE_API_KEY não foi encontrada. Verifique seu arquivo .env")


genai.configure(api_key=api_key)


def analyze_email_with_gemini(email_content):
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        prompt = f"""
        Aja como um assistente de produtividade para análise de emails.
        Sua tarefa é analisar o email fornecido e retornar duas coisas:
        1.  Uma classificação: 'Produtivo' ou 'Improdutivo'.
            -   'Produtivo': Emails que exigem uma ação, resposta específica, ou são diretamente relacionados a trabalho.
            -   'Improdutivo': Emails pessoais, spam, felicitações, ou que não necessitam de uma ação de trabalho imediata.
        2.  Uma sugestão de resposta curta e adequada ao contexto do email.

        Formate a sua saída EXATAMENTE da seguinte forma, sem adicionar nada extra:
        CLASSIFICACAO: [aqui a sua classificacao]
        RESPOSTA: [aqui a sua sugestão de resposta]

        ---
        EMAIL PARA ANÁLISE:
        "{email_content}"
        ---
        """
        response = model.generate_content(prompt)

        if not hasattr(response, 'text'):
           
            return "Análise Bloqueada", "A resposta da IA foi bloqueada por motivos de segurança."

        text_response = response.text.strip()
        classification_part = text_response.split("CLASSIFICACAO:")[1].split("RESPOSTA:")[0].strip()
        response_part = text_response.split("RESPOSTA:")[1].strip()

        return classification_part, response_part
    
    except Exception as e:
        
        print(f"Erro capturado")
        print(f"ERRO: {e}")
        
        return "Erro na Análise", "Ocorreu um problema ao comunicar com a IA. Verifique o terminal para mais detalhes."


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    classification, suggested_response = analyze_email_with_gemini(email_text)
    return render_template('index.html',
                           email_text=email_text,
                           classification=classification,
                           suggested_response=suggested_response)


if __name__ == '__main__':
    app.run(debug=True)
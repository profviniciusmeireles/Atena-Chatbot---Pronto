#pip install google-generativeai
#pip install streamlit

import os
import streamlit as st
import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a chave de API do Google Cloud
os.environ['GOOGLE_API_KEY'] = os.getenv("GEMINI_API_KEY")

# Configuração do genai com a chave de API do Google Cloud
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


#LLM (large language model) do Gemini 
llm = genai.GenerativeModel('gemini-1.0-pro')

#Configuração da Página do APP:

st.set_page_config(page_title="Atena ChatBot", page_icon= "🤖") 

# Style: OCULTAR APPS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)



#Streamlit oferece vários elementos que facilitam a criação de interfaces gráficas do usuário para chatbots. 
#Um dos elementos que usaremos será o estado da sessão (session_state) para armazenar o histórico do chat para ele aparecer no nosso aplicativo. 
#Primeiro, verificamos se o estado da sessão tem a chave messages indicando que a interação já foi iniciada. Se não tiver, ela será inicializada como uma lista contendo apenas uma frase inicial do bot (content).
def main():

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role":"assistant",
                "content":"Olá! o que posso te ajudar?"
            }
        ]

    #Depois, adicionamos um for loop para iterar pela lista com o histórico do chat e exibir cada mensagem no contêiner de mensagens do nosso aplicativo.

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    #Em seguida, usamos um elemento do tipo chat_input, para receber as questões do usuário do aplicativo.  
    query = st.chat_input("Oi, me pergunte qualquer coisa")

       
    #Na sequência, definimos uma função que acessa o LLM através da Gemini API e obtém a resposta para as consultas do usuário. 
    #A função também será usada para armazenar as consultas e as respostas da interação.
    def function_llm(query):
        ''' Função que acessa o LLM, gera a resposta e salva a interação.'''

        # acessa o LLM para gerar uma resposta
        response = llm.generate_content(query)

        # Mostra as mensagens do bot
        with st.chat_message("assistant"):
            st.markdown(response.text)
        
        # Salva as mensagens do usuário
        st.session_state.messages.append(
            {
                "role":"user",
                "content": query
            }
        )

        # Salva as mensagens do bot
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content": response.text
            }
        )

    # Após isso, precisamos definir um comando para verificar se existe uma mensagem do usuário no nosso aplicativo. 
    #Em caso afirmativo, ela é exibida e a função definida acima é chamada. Esse trecho encerra nosso aplicativo.  
    if query:
        # Mostra a mensagem do usuário
        with st.chat_message("user"):
            st.markdown(query)
            
        # chama a função que acessa o LLM
        function_llm(query)
        # Exibir o histórico de mensagens no sidebar
    with st.sidebar:
        st.write("Recentes")
        for msg in st.session_state.messages:
            if msg['role'] == 'user':
                st.info(f"✉ {msg['content']}")
           
#função para limpar historico do chat
def clear_chat_history():
    st.session_state.messages = [
        {
        "role": "assistant", 
        "content": "Olá! o que posso te ajudar?"
        }
    ]


st.sidebar.button("➕ Nova conversa", on_click=clear_chat_history)

#st.logo("img/logo.png")
      
if __name__ == "__main__":
    main() 
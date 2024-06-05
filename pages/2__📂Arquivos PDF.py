import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

import warnings
warnings.filterwarnings("ignore")

#CARREGAR API KEY
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#CARREGAR PDF (pecorre cada pagina do pdf e extrair os textos)
def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:    #ler arquivo pdf
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:   #ler as paginas do arquvo pdf selecionado
            text+= page.extract_text()  #extrair os textos das paginas
    return text

#função para dividir os textos em menores partes (10.000 palavras ou tokens, )
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks=text_splitter.split_text(text)   #divide o texto em pedaços menores
    return chunks

#convertendo os pedaços de textos para vetores
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") #criar o objeto que carrega o modelo Embeddings
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings) #incorporar os pedaços de textos (text_chunks) com os seus embeddings salva em armazenamento de vetor (vector+_store)
    vector_store.save_local("faiss_index")  #salvar o vetor_store no disco local
   

def get_conversational_chain():         #obter a cadeia de conversação utizando o prompt e modelo do algoritmo
    prompt_template = """
    Responda à pergunta o mais detalhadamente possível a partir do contexto fornecido, certifique-se de fornecer todos os detalhes, se a resposta não estiver correta
    fornecido o contexto, basta dizer "a resposta não está disponível no contexto", não forneça a resposta errada\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    #CRIAR O MODELO GOOGGLE GENERATIVE
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain=load_qa_chain(model, chain_type="stuff", prompt=prompt) #load the chain de resumo dos texto

    return chain

#função para criar o prompt de contexto da entrada do usuário como uma pergunta.
def user_input(user_question): 
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)   #carrega o arquivo vector: faiss_index
    docs = new_db.similarity_search(user_question)         #busca de similaridade com base da pergunta usual do usuário. 

    chain = get_conversational_chain()                      #chama a função de conversação

    
    response = chain(                                       #retorno da resposta de busca no algoritmo Gemini
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
   
    return response

#função para limpar historico do chat
def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! o que posso te ajudar?"}]

#criar a aplicativo Streamlit
def main():
 
    st.set_page_config(page_title="Atena ChatBot", page_icon= "🤖") 
 
    with open('style.css')as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    with st.sidebar:
        pdf_docs = st.file_uploader("Carregue seus arquivos PDF e clique no botão Processar", accept_multiple_files=True)
        
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("⏳ Processar", help='Enviar e processar arquivo(s) PDF'):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Feito")
    with col2:
            st.button('🗑 Histórico', on_click=clear_chat_history, help='Limpar o histórico')

    # Chat input
    # Placeholder for chat messages

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "Olá! o que posso te ajudar?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Display chat messages and bot response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Analisando..."):
                response = user_input(prompt)
                placeholder = st.empty()
                full_response = ''
                for item in response['output_text']:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        if response is not None:
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)

if __name__ == "__main__":
    main()    

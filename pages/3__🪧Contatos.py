import streamlit as st

#Apps

st.set_page_config(page_title="Atena ChatBot", page_icon= "🤖") 

# Style: OCULTAR APPS
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#pages
st.markdown("<h1 style='text-align: center; color: red;'>📨Contatos</h1>", unsafe_allow_html=True)
st.subheader("", divider='blue')

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("icons/whatsapp.png", caption="28 99918-3961", width=90)

with col2:
    st.image("icons/gmail.png", caption="viniciusmeireles@gmail.com", width=100)

with col3:
    st.image("icons/location.png", caption="Ibatiba/ES", width=90)    

with col4:
    st.image("icons/linkedin.png",caption= "/pviniciusmeireles", width=90)

st.subheader("", divider='blue')


col1, col2 = st.columns(2)
with col1:
    st.image("img/logo1.jpg", width=140, caption="Google Gemini") 
with col2:
    st.image("img/logo.png", width=320, caption="Desenvolvimento de Apps com Inteligência Articial")
     

#st.toast("Página atualizada!", icon='✅')
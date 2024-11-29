import yaml
import streamlit as st
import roles.admin.admin as admin

import roles.student.student as student
import roles.student.aulas as aulas_student
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

st.set_page_config(
    page_icon="📓",
    page_title="Cursinho"
)

with open('src/config.yaml', "r", encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

def main():
    # Adicione uma variável para controlar a página atual
    page = None
    
    # sidebar
    with st.sidebar:
        page = option_menu(None, ["Home", "Aulas", 'Settings', "Sair"], 
            icons=['house', "bi-youtube", 'gear', 'box-arrow-right'], menu_icon="cast", default_index=0)
        
        if page == "Sair":
            authenticator.logout()
    
    # Renderize a página correta com base na seleção
    if page == "Aulas":
        aulas_student.aulas()  # Chame a função de aulas em uma página separada
    #página do admin   
    elif "admin" in st.session_state['roles']:
        admin.admin_page(st.session_state["name"], authenticator)
    #página do estudante
    elif "student" in st.session_state['roles']:
        student.student_page(st.session_state["name"], authenticator)

try:
    authenticator.login()
    if st.session_state['authentication_status']:
        main()
    elif st.session_state['authentication_status'] is False:
        st.error('Usuário/senha está incorreta')
    elif st.session_state['authentication_status'] is None:
        st.warning('Por favor, coloque seu usuário e senha')
        
except Exception as e:
    st.error(e)
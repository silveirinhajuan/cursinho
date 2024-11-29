import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu



def admin_page(name, authenticator):
    with st.sidebar:
        selected = option_menu(None, ["Home", 'Settings', "Sair"], 
            icons=['house', 'gear', 'box-arrow-right'], menu_icon="cast", default_index=1)
        if selected == "Sair":
            authenticator.logout()
    st.title(f'Olá {name}!')
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu



def admin_page(name, authenticator):
    # horizontal Menu
    selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    st.title(f'Olá {name}!')
    
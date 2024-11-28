import streamlit as st
from streamlit_option_menu import option_menu

def student_page(name):
    with st.sidebar:
        selected = option_menu(None, ["Home", 'Settings'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
    st.title(f'Olá {name}!')
    
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu



def student_page(name, authenticator):
    st.title(f'Olá, {name}!')
    
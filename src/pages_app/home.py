import streamlit as st
from utils.utils import return_greeting, weekly_day, current_date

def homepage():
    st.header(f'{return_greeting()}, {st.session_state['name']}')
    st.subheader(f'{weekly_day()}, {current_date()}')
    
    st.divider()
    
    st.write("terá um blog aqui...")
    
    
homepage()
    
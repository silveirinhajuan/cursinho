import yaml
import streamlit as st
from roles.admin import admin
from roles.student import student
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader

with open('src/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

def main():
    
    with st.sidebar:
        selected = option_menu(None, ["Home", 'Settings', "Sair"], 
            icons=['house', 'gear', 'box-arrow-right'], menu_icon="cast", default_index=1)
        if selected == "Sair":
            authenticator.logout()

    # horizontal Menu
    selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")

#Iframe para testar posteriormente
#st.components.v1.iframe("https://player.vimeo.com/video/1034342025?title=0&amp;byline=0&amp;portrait=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479", width=720, height=1080)

try:
    authenticator.login()
    if st.session_state['authentication_status']:
        main()
except Exception as e:
    st.error(e)
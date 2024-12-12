import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

###Pages
#Student area
home_page = st.Page(
    page='pages_app/home.py',
    title='Início',
    icon=':material/home:',
)

account_page = st.Page(
    page="pages_app/account.py",
    title="Conta",
    icon=":material/account_circle:",
)

settings_page = st.Page(
    page="pages_app/settings.py",
    title="Configurações",
    icon=":material/settings:",
)

disciplines_page = st.Page(
    page='pages_app/disciplines.py',
    title="Disciplinas",
    icon=":material/auto_stories:"
)

#Home page configuration
st.set_page_config(
    page_icon="📓",
    page_title="Cursinho"
)

#Authenticator 
with open('src/config.yaml', "r", encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
def main():
    #Navigation pages
    pg = st.navigation(
        {
            "🏠 Início":[home_page],
            "🎬 Aulas":[disciplines_page],
            "⚡ Configurações":[account_page, settings_page],
        }
    )
    
    pg.run()
    
#Logins
try:
    authenticator.login()
    if st.session_state['authentication_status']:
        main()
        authenticator.logout(location="sidebar")
    elif st.session_state['authentication_status'] is False:
        st.error('Usuário/senha está incorreta')
    elif st.session_state['authentication_status'] is None:
        st.warning('Por favor, coloque seu usuário e senha')
        
except Exception as e:
    st.error(e)
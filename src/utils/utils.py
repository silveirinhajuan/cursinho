import streamlit as st
from datetime import datetime, timedelta, timezone

### VARIABLES ###
# Date and time variables
DIFERENCE = timedelta(hours=-3)
TIME_ZONE = timezone(DIFERENCE)

################################

### FUNCTIONS ###
#Date and time functions
def return_greeting():
    current_time = (datetime.now().astimezone(TIME_ZONE)).hour

    if 6 <= current_time < 12:
        return "🌞 Bom dia"
    elif 12 <= current_time < 18:
        return "📘 Boa tarde"
    elif 18 <= current_time < 24:
        return "🌃 Boa noite"
    else:
        return "🤨 Boa madrugada"
    
def weekly_day():
    week = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
    weekly_day = week[(datetime.now().weekday())]
    return weekly_day

def current_month():
    year = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    print(((datetime.now()).month - 1))
    return year[((datetime.now()).month - 1)]

def current_date():
    return f"{(datetime.now()).day} de {current_month().lower()} de {(datetime.now()).year}"
    
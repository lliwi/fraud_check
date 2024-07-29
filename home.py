import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

st.set_page_config(
    page_title="Homepage",
    page_icon="🏡",
    layout="centered",
    initial_sidebar_state="expanded"
)

if all (key not in st.session_state.keys() for key in ('username', 'pwd', 'pwd_correct', 'form_submitted')):
    st.session_state['username'] = ""
    st.session_state['pwd'] = ""
    st.session_state['pwd_correct'] = False
    st.session_state['form_submitted'] = False

def check_login():
    st.session_state['form_submitted'] = True

    if (
        st.session_state["username"] in st.secrets["passwords"]
        and 
        st.session_state["pwd"] == st.secrets["passwords"][st.session_state["username"]]
    ):
        st.session_state['pwd_correct'] = True
        st.session_state['pwd'] = ""
        st.session_state['username'] = ""
    else:
        st.session_state['pwd_correct'] = False

def display_login_form():
    with st.form("login_form"):
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="pwd")

        st.form_submit_button("Login", on_click=check_login)

if (st.session_state['pwd_correct'] == False and st.session_state['form_submitted'] == False):
    display_login_form()
elif (st.session_state['pwd_correct'] == False and st.session_state["form_submitted"] == True):
    display_login_form()
    st.error("Invalid user/password")
elif (st.session_state['pwd_correct'] == True and st.session_state["form_submitted"] == True):
    st.image('./media/banner.png')

    if 'IPQS_API_KEY' not in st.session_state:
        #load_dotenv()
        st.session_state.IPQS_API_KEY = st.secrets["IPQS_API_KEY"]
        st.session_state.APILAYER_KEY = st.secrets["APILAYER_KEY"]
        st.session_state.SERPAPI_KEY = st.secrets["SERPAPI_KEY"]

    d = {'Recurso':['OSINT Framework','IPQS','APILayer','holele','Intelligence X','numverufy','emailrep','sherlock','maltego','trustfull','pipl'], 
    'link':['https://osintframework.com','https://www.ipqualityscore.com','https://apilayer.com','https://github.com/megadose/holehe','https://intelix.io','https://numverify.com','https://emailrep.io','https://github.com/sherlock-project/sherlock','https://www.maltego.com','https://trustfull.com','https://pipl.com']}
    df = pd.DataFrame(data=d)
    
    with st.expander("Recursos OSINT"):
        st.dataframe(df,hide_index=True)
else:
    display_login_form()

#st.write(st.session_state)
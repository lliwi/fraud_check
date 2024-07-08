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



if __name__ == "__main__":

    #st.title("Homepage")
    st.image('./media/banner.png')

    if 'IPQS_API_KEY' not in st.session_state:
        load_dotenv()
        st.session_state.IPQS_API_KEY = os.getenv("IPQS_API_KEY")
        st.session_state.APILAYER_KEY = os.getenv("APILAYER_KEY")
        #st.session_state.SERPAPI_KEY = os.getenv("SERPAPI_KEY")

    d = {'Recurso':['OSINT Framework','IPQS','APILayer','holele','Intelligence X','numverufy','emailrep','sherlock','maltego','trustfull','pipl'], 
    'link':['https://osintframework.com','https://www.ipqualityscore.com','https://apilayer.com','https://github.com/megadose/holehe','https://intelix.io','https://numverify.com','https://emailrep.io','https://github.com/sherlock-project/sherlock','https://www.maltego.com','https://trustfull.com','https://pipl.com']}
    df = pd.DataFrame(data=d)
    
    with st.expander("Recursos OSINT"):
        st.dataframe(df,hide_index=True)
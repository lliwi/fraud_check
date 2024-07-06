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
import streamlit as st
import os
import tempfile
import base64
from pypdf import PdfReader
import spacy
from spellchecker import SpellChecker
import re
from streamlit_extras.switch_page_button import switch_page

if all (key not in st.session_state.keys() for key in ('username', 'pwd', 'pwd_correct', 'form_submitted')):
    st.session_state['username'] = ""
    st.session_state['pwd'] = ""
    st.session_state['pwd_correct'] = False
    st.session_state['form_submitted'] = False

if (st.session_state['pwd_correct'] == False and st.session_state['form_submitted'] == False):
    switch_page("home")
elif (st.session_state['pwd_correct'] == False and st.session_state["form_submitted"] == True):
    switch_page("home")
    #st.error("Invalid user/password")
elif (st.session_state['pwd_correct'] == True and st.session_state["form_submitted"] == True):
    st.image('./media/banner.png')


    uploaded_file = st.file_uploader("File upload", type="pdf")
    if uploaded_file:
        with st.spinner('Cargando datos ...'):
            temp_dir = tempfile.mkdtemp()
            path = os.path.join(temp_dir, uploaded_file.name)

            with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())
            fp = open(path, 'rb')
            reader = PdfReader(fp)

            for page in reader.pages:
                text = page.extract_text()
                text = text + text

            spell=SpellChecker(language='es')
            docx=re.findall("[a-zA-Z]+",text)

            faltas = spell.unknown(docx)
            palabras = len(text)
            count = 0
            for word in faltas:
                if spell.candidates(word):
                    count = count + 1
            
            st.markdown(f"**Palabras:** {palabras}")
            st.markdown(f"**Faltas:** {count}")

            with st.expander("Detail"):
                for word in faltas:
                    if spell.candidates(word):
                        st.markdown(f"{word} --> {spell.candidates(word)}")

            with st.expander("RAW data"):
                st.write(text)
        

            with st.expander("PDF file"):
                with open(path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

                    
                st.markdown(pdf_display, unsafe_allow_html=True)  

else:
    #display_login_form()
    switch_page("home")
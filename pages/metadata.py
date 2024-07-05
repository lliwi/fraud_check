from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import streamlit as st
import os
import tempfile
from dateutil import parser
import base64


st.image('./media/banner.png')

uploaded_file = st.file_uploader("File upload", type="pdf")
if uploaded_file:
    temp_dir = tempfile.mkdtemp()
    path = os.path.join(temp_dir, uploaded_file.name)

    with open(path, "wb") as f:
        f.write(uploaded_file.getvalue())
    fp = open(path, 'rb')
    parsed_file = PDFParser(fp)
    doc = PDFDocument(parsed_file)

    for element in doc.info[0]:
        try:
            if "Date" in element:
                element_val =  element_val = parser.parse(doc.info[0][element].decode('utf-8')[2:14])
                st.write(f"**{element}:** {element_val}")
            else:
                try:
                    element_val = doc.info[0][element].decode('utf-8')
                    st.markdown(f"**{element}:** {element_val}")
                except:
                    element_val = doc.info[0][element].decode('utf-16')
                    st.markdown(f"**{element}:** {element_val}")
        except:
            pass


    with st.expander("RAW data"):
         st.write(doc.info[0])
 

    with st.expander("PDF file"):
        with open(path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

            
        st.markdown(pdf_display, unsafe_allow_html=True)  
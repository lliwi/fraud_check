import streamlit as st
import os

st.image('./media/banner.png')

mail = st.text_input('Email', placeholder="foo@bar.com")

if mail:
    with st.spinner('Cargando datos ...'):
        info = os.popen("holehe --no-color "+ mail).read()
        info = info.replace("Twitter : @palenath", "")
        info = info.replace("Github : https://github.com/megadose/holehe","")
        info = info.replace("For BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ", "")
        info = info.replace("[-] Please enter a target email ! ", "")
        info = info.replace("Example : holehe email@example.com", "")
        info = info.replace("***************************", "")
        info = info.replace(mail, "")
        info = info.replace("[+] Email used, [-] Email not used, [x] Rate limit", "")
        info = info.replace("[H[J", "")

        
        for domain in info.split("\n"):
            if domain.startswith("[+]"):
                st.write(domain)
   


    with st.expander("RAW data"):
         for domain in info.split("\n"):
            if domain is not "\n":
                st.write(domain)


st.markdown(f"*Datos obtenidos con el software [holehe](https://github.com/megadose/holehe)*")
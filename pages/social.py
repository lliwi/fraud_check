import streamlit as st
import os
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
                if domain != "\n":
                    st.write(domain)


    st.markdown(f"*Datos obtenidos con el software [holehe](https://github.com/megadose/holehe)*")

else:
    #display_login_form()
    switch_page("home")
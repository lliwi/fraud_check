import streamlit as st
import requests
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

    phone_txt = st.text_input("Telefono", placeholder="34666554422", key="phone")
    if phone_txt:
        with st.spinner('Cargando datos ...'):
            r = requests.get("https://api.apilayer.com/number_verification/validate?number=" + phone_txt , headers={'apikey':st.session_state.APILAYER_KEY})
            response = r.json()
            
            st.markdown(f"**Valid:** {response['valid']}")
            st.markdown(f"**Number:** {response['number']}")
            st.markdown(f"**Country code:** {response['country_code']}")
            st.markdown(f"**Country:** {response['country_name']}")
            st.markdown(f"**City:** {response['location']}")
            st.markdown(f"**Carrier:** {response['carrier']}")
            st.markdown(f"**Line type:** {response['line_type']}")


            with st.expander("RAW response"):
                st.write(response)
            

    st.markdown(f"*Datos obtenidos de [APILayer](https://apilayer.com) FreeAPI 100 consultas al mes*")

else:
    #display_login_form()
    switch_page("home")
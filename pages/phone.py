import streamlit as st
import json
import requests
from typing import Union
from wtforms.validators import Email
import json
from streamlit_extras.switch_page_button import switch_page

class IPQS:
    key =  st.session_state.IPQS_API_KEY
    def phone_number_api(self, phonenumber: str, vars: dict = {}) -> dict:
        url = 'https://www.ipqualityscore.com/api/json/phone/%s/%s' %(self.key, phonenumber)
        x = requests.get(url, params = vars)
        return (json.loads(x.text))
    
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
    countries = {'ES'};

    additional_params = {
            'country' : countries
        }

    if phone_txt:
        with st.spinner('Cargando datos ...'):
            ipqs = IPQS()
            response  = ipqs.phone_number_api(phone_txt, additional_params)


            try:
                
                    st.markdown(f"**Message:** {response['message']}")
                    #st.markdown(f"**Success:** {response['success']}")
                    #st.markdown(f"**Valid:** {response['valid']}")
                    st.progress(response['fraud_score'], text="**Fraud score:**")
                    st.markdown(f"**Recent abuse:** {response['recent_abuse']}")
                    st.markdown(f"**VOIP:** {response['VOIP']}")
                    st.markdown(f"**Carrier:** {response['carrier']}")
                    st.markdown(f"**Line type:** {response['line_type']}")
                    st.markdown(f"**Country:** {response['country']}")
                    #st.markdown(f"**City:** {response['city']}")
                    st.markdown(f"**Region:** {response['region']}")

            except:
                    pass


            with st.expander("RAW response"):
                st.write(response)

    st.markdown(f"*Datos obtenidos de [IPQS](https://www.ipqualityscore.com) FreeAPI 20 consultas al dia*")

else:
    #display_login_form()
    switch_page("home")
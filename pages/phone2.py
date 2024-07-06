import streamlit as st
import requests

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
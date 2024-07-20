import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from ignorant.modules.shopping.amazon import amazon
from ignorant.modules.social_media.instagram import instagram
import httpx
import asyncio
import json


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

    phone = st.text_input('Telefono', placeholder="600111222")
    amazon_resp = []
    instagram_resp = []
    snapchat_resp = []

    async def amazon_req():
        country_code="34"
        client = httpx.AsyncClient()
        await amazon(phone, country_code, client, amazon_resp)
        await client.aclose()

    async def instagram_req():
        country_code="34"
        client = httpx.AsyncClient()

        await instagram(phone, country_code, client, instagram_resp)
        await client.aclose()
        

    if phone:
        with st.spinner('Cargando datos ...'):
            asyncio.run(amazon_req())
            amazon = amazon_resp[0]['exists']
            st.write(f"**Amazon:** {amazon}")

            asyncio.run(instagram_req())
            instagram = instagram_resp[0]['exists']
            st.write(f"**Instagram:** {instagram}")



        with st.expander("RAW data"):
            st.write(amazon_resp)
            st.write(instagram_resp)


    st.markdown(f"*Datos obtenidos con el software [ignorant](https://github.com/megadose/ignorant)*")
    st.markdown(f"*La fiabilidad del resultado no es muy alta*")

else:
    #display_login_form()
    switch_page("home")
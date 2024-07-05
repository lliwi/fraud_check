import streamlit as st
import json
import requests
from typing import Union
from wtforms.validators import Email
import json

os.environ['API_KEY']


class Validate(object):
    """
    Class for interacting with the IPQualityScore API.

    Attributes:
        key (str): Your IPQS API key.
        format (str): The format of the response. Default is 'json', but you can also use 'xml'.
        base_url (str): The base URL for the IPQS API.

    Methods:
        email_validation_api(email: str, timeout: int = 1, fast: str = 'false', abuse_strictness: int = 0) -> str:
            Returns the response from the IPQS Email Validation API.
    """

    key = None
    format = None
    base_url = None

    def __init__(self, key, format="json") -> None:
        self.key = key
        self.format = format
        self.base_url = f"https://www.ipqualityscore.com/api/{self.format}/"

    def email_validation_api(self, email: str, timeout: int = 7, fast: str = 'false', abuse_strictness: int = 0) -> str:
        """
        Returns the response from the IPQS Email Validation API.

        Args:
            email (str):
                The email you wish to validate.
            timeout (int):
                Set the maximum number of seconds to wait for a reply from an email service provider.
                If speed is not a concern or you want higher accuracy we recommend setting this in the 20 - 40 second range in some cases.
                Any results which experience a connection timeout will return the "timed_out" variable as true. Default value is 7 seconds.
            fast (str):
                If speed is your major concern set this to true, but results will be less accurate.
            abuse_strictness (int):
                Adjusts abusive email patterns and detection rates higher levels may cause false-positives (0 - 2).

        Returns:
            str: The response from the IPQS Email Validation API.
        """

        url = f"{self.base_url}email/{self.key}/{email}"

        params = {
            "timeout": timeout,
            "fast": fast,
            "abuse_strictness": abuse_strictness
        }

        response = requests.get(url, params=params)
        return response.text

st.image('./media/banner.png')
v = Validate(API_KEY)
email_txt = st.text_input("Email", placeholder="foo@bar.com", key="email")

    
      
if email_txt:
    email = email_txt
    response = json.loads(v.email_validation_api(email))
    try:
        #Success
        st.markdown(f"**Sucess:**")
        if response['success'] == True:
            st.image('./media/check.png',width=20)
        else:
            st.image('./media/cross.png')
        #Valid
        st.markdown(f"**valid:**")
        if response['valid'] == True:
            st.image('./media/check.png',width=20)
        else:
            st.image('./media/cross.png')
        #Nombre
        st.markdown(f"**Nombre:**")
        st.write(response['first_name'])
        #Fraud score
        st.progress(response['fraud_score'], text="**Fraud score:**")
        #Leaked
        st.markdown(f"**leaked:**")
        if response['leaked'] == True:
            st.image('./media/check.png',width=20)
        else:
            st.image('./media/cross.png')
        #st.markdown(f"**User activity:** {response['user_activity']}")
    except:
        pass


    with st.expander("RAW response"):
        st.write(response)
   
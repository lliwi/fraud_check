import streamlit as st
import json
import requests
from typing import Union
from wtforms.validators import Email
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


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

    
    def phone_number_validation_api(self, phone_number: str, country: Union[str, list], strictness: int = 0) -> str:
        """
        Returns the response from the IPQS Phone Number Validation API.

        Args:
            phone_number (str):
                The phone number you wish to validate.
            country (str or list):
                You can optionally provide us with the default country or countries this phone number is suspected to be associated with.
                Our system will prefer to use a country on this list for verification or will require a country to be specified in the event the phone number is less than 10 digits.
            strictness (int):
                Adjusts the strictness of the phone number validation. Higher levels may cause false-positives (0 - 2)

        Returns:
            str: The response from the IPQS Phone Number Validation API.
        """

        url = f"{self.base_url}phone/{self.key}/{phone_number}"

        params = {
            "country": country,
            "strictness": strictness
        }

        response = requests.get(url, params=params)
        return response.text
st.image('./media/banner.png')
v = Validate(API_KEY)


    
    

phone_txt = st.text_input("Telefono", placeholder="34666554422", key="phone")

    
    
   

if phone_txt:
    phone = phone_txt
    response = json.loads(v.phone_number_validation_api(phone, 'ES'))

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
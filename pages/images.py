import streamlit as st
from serpapi.google_search import GoogleSearch
import json
import mimetypes
from streamlit import runtime
from streamlit.runtime import caching
import os
import tempfile
from streamlit_js_eval import get_page_location
import time
from streamlit_extras.switch_page_button import switch_page
from PIL import Image, ImageChops

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

    def serve_image(image, image_id):
        mimetype, _ = mimetypes.guess_type(image)
        if mimetype is None:
            mimetype = "application/octet-stream"
        url = runtime.get_instance().media_file_mgr.add(image, mimetype, image_id)
        caching.save_media_data(image, mimetype, image_id)
        return(url)


    def buscar_imagen(query):
        params = {
        'api_key': st.session_state.SERPAPI_KEY ,
        'engine': 'google_lens',
        'url': query,
        'hl': 'es',
        're': 'df'
        }   

        search = GoogleSearch(params)                   # data extraction on the SerpApi backend
        google_lens_results = search.get_dict()         # JSON -> Python dict
        try:
            del google_lens_results['search_metadata']
            del google_lens_results['search_parameters']
        except:
            pass

        return json.dumps(google_lens_results, indent=2, ensure_ascii=False)
    
    def compare_images(image1, image2):
        img1 = Image.open(image1)
        img2 = Image.open(image2)
        diff = ImageChops.difference(img1, img2)
        st.write(diff.getbbox())
        return diff.getbbox() is None

    st.image('./media/banner.png')


    uploaded_file = st.file_uploader("File upload")
    if uploaded_file:
        with st.spinner('Cargando datos ...'):
            temp_dir = tempfile.mkdtemp()
            path = os.path.join(temp_dir, uploaded_file.name)
            st.image(uploaded_file)
            with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())
            server_host = "localhost"
            url = serve_image(path, 'please_do_not_crash')
            try:
                server_host = get_page_location()['host']
            except:
                pass

            r = buscar_imagen('http://' + server_host + '/~/+' + url)
            
            #time.sleep(2)
            try:
                response = json.loads(r)
                
                for match in response['visual_matches']:
                    st.markdown(f"***Title:*** {match['title']}")
                    st.markdown(f"***Link:*** {match['link']}")
                    st.markdown(f"***Source:*** {match['source']}")
                    st.image(match['thumbnail'])
                    compare_images(uploaded_file, match['thumbnail'])
            

                with st.expander('RAW'):
                    st.write(response)
            except:
                st.write('No se encontraron resultados')
else:
    #display_login_form()
    switch_page("home")
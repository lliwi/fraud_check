import streamlit as st
from serpapi.google_search import GoogleSearch
import json
import mimetypes
from streamlit import runtime
from streamlit.runtime import caching
import os
import tempfile
from streamlit_js_eval import get_page_location


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
    'hl': 'en',
    }   

    search = GoogleSearch(params)                   # data extraction on the SerpApi backend
    google_lens_results = search.get_dict()         # JSON -> Python dict
    try:
        del google_lens_results['search_metadata']
        del google_lens_results['search_parameters']
    except:
        pass

    return json.dumps(google_lens_results, indent=2, ensure_ascii=False)

st.image('./media/banner.png')


uploaded_file = st.file_uploader("File upload")
if uploaded_file:
    with st.spinner('Cargando datos ...'):
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, uploaded_file.name)
        st.image(uploaded_file)
        with open(path, "wb") as f:
            f.write(uploaded_file.getvalue())

        url = serve_image(path, 'please_do_not_crash')
        response = buscar_imagen('http://' + get_page_location()['host']  + '/~/+' + url)
        
        st.write(type(response))
       

        with st.expander('RAW'):
            st.write(response)
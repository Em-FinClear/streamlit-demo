import streamlit as st
import st_pages as stp
import pandas as pd


def authenticated():

    stp.add_page_title()
        # Title
    st.title("Map of Sydney")

    map_data = pd.DataFrame({
        'lat': [-33.8688],
        'lon': [151.2093]
    })

    st.map(map_data)


def main():

    if 'hidden_pages' not in st.session_state:
        st.session_state['hidden_pages'] = ['Charts', 'ChatGPT API', 'Map']
        
    # If a user lands on this page directly
    if 'authentication_status' in st.session_state:

        if st.session_state['authentication_status']:
            authenticated()
        else:
            st.warning('Please return to Home page to log in')
            stp.hide_pages(st.session_state['hidden_pages'])
    else:
        st.warning('Please return to Home page to log in')
        stp.hide_pages(st.session_state['hidden_pages'])

main()
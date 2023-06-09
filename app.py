import streamlit as st
import streamlit_authenticator as stauth
import st_pages as stp

def authenticated():

    # Add page title and icon to page
    # stp.add_page_title()

    st.session_state.authenticator.logout('Logout', 'sidebar')
    st.write("# Welcome to FinClear's Streamlit! 👋")
    # st.sidebar.success("Select a page above.")

def load_secrets():

    # Authentication
    credentials = dict(st.secrets.auth.credentials) # Must copy this as it is modified by stauth
    cookie = st.secrets.auth.cookie
    preauthorised = st.secrets.auth.preauthorised

    if 'authenticator' not in st.session_state:
        st.session_state['authenticator'] = stauth.Authenticate(credentials, cookie.name, cookie.key, cookie.expiry_days, preauthorised)

    if 'openai_api_key' not in st.session_state:
        st.session_state['openai_api_key'] = st.secrets.api_keys.openai

def main():

    # Load secrets
    load_secrets()

    # Set up pages
    stp.show_pages(
        [
            stp.Page('app.py', 'Home', '🏠'),
            stp.Page('sub_pages/charts.py', 'Charts', '📊'),
            stp.Page('sub_pages/chatGPT.py', 'ChatGPT API', '🧠'),
            stp.Page('sub_pages/map.py', 'Map', '🗺️')
            # stp.Section('Section name', '🔐')
        ]
    )

    # Hide pages if not authenticated
    if 'hidden_pages' not in st.session_state:
        st.session_state['hidden_pages'] = ['Charts', 'ChatGPT API', 'Map']
        
    # Run authentication window
    st.session_state.authenticator.login('Login')

    if st.session_state['authentication_status']:
        authenticated()

    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
        stp.hide_pages(st.session_state['hidden_pages'])

    elif st.session_state["authentication_status"] == None:
        st.info('Please enter your username and password')
        stp.hide_pages(st.session_state['hidden_pages'])

main()
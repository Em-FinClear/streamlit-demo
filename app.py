import streamlit as st
import streamlit_authenticator as stauth

def main():

    credentials = dict(st.secrets.auth.credentials)
    cookie = st.secrets.auth.cookie
    preauthorised = st.secrets.auth.preauthorised

    authenticator = stauth.Authenticate(credentials, cookie.name, cookie.key,
                                        cookie.expiry_days, preauthorised)
    
    name, authentication_status, username = authenticator.login('Login', 'main')

    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'sidebar')
        # st.write(f'Welcome *{st.session_state["name"]}*')
        # st.title('Some content')
        st.set_page_config(page_title="Home", page_icon="🏠")
        st.write("# Welcome to FinClear's Streamlit! 👋")
        st.sidebar.success("Select a page above.")

    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')

    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')

main()
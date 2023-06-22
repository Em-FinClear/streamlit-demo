import streamlit as st
from toolbox import hi

def app():

    # Configure page
    page = 'home'
    st.title(f'{st.session_state.app.pages[page].icon} {st.session_state.app.pages[page].title}')
    st.header("Welcome to FinClear's Streamlit! 👋")
    # st.sidebar.success("Select a page above.")

    with st.form('toolbox_hello'):
        input_text = st.text_area('What should I call you?')
        submit_button = st.form_submit_button('Submit')

    # Process the input text when the button is clicked
    if submit_button:
        st.write(hi.hello(input_text))

import streamlit as st
import st_pages as stp
import openai

def ChatGPT(user_query, out_token):

    model_engine = "text-davinci-003"
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = out_token,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0].text
    return response

def authenticated():

    stp.add_page_title()

    openai.api_key = st.session_state['openai_api_key']

    output_size = st.radio(label = "What kind of output do you want?", 
                           options= ["To-The-Point", "Concise", "Detailed"])
    
    out_token = 1024

    if output_size == "To-The-Point":
        out_token = 50
    elif output_size == "Concise":
        out_token = 128
    else:
        out_token = 516

    with st.form('text_input_form'):
        input_text = st.text_area('Enter your query:')
        submit_button = st.form_submit_button('Submit')

    # Process the input text when the button is clicked
    if submit_button:
        user_query = input_text

        if user_query != ":q" and user_query != "":
            # Pass the query to the ChatGPT function
            response = ChatGPT(user_query, out_token)
            return st.write(f"{user_query} {response}")


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
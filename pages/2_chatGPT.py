import streamlit as st
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

def main():

    st.set_page_config(page_title="ChatGPT API", page_icon="🧠")

    openai.api_key = st.secrets.api_keys.openai

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

# main()
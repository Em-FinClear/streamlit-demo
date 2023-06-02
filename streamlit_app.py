import streamlit as st
import pandas as pd
import openai
import plotly.express as px


def home_page():

    # Title
    st.title("Demo Streamlit App")

    # Section 1 - Line Chart
    st.header("Section 1: Line Chart")

    # Assume we have some time series data
    df_line = pd.DataFrame({
      'date': pd.date_range(start='1/1/2020', periods=100),
      'value': (pd.Series(range(100)) + pd.Series(range(100)).cumsum()).tolist()
    })

    fig1 = px.line(df_line, x='date', y='value', labels={'value':'Values Over Time'})
    st.plotly_chart(fig1)

    # Section 2 - Pie Chart
    st.header("Section 2: Pie Chart")

    # Assume we have some categorical data
    df_pie = pd.DataFrame({
      'Fruit': ['Apples', 'Bananas', 'Cherries', 'Dates'],
      'Amount': [15, 30, 8, 6]
    })

    fig2 = px.pie(df_pie, values='Amount', names='Fruit', title='Fruit Consumption')
    st.plotly_chart(fig2)

    # Section 3 - Personal Details
    st.header("Section 3: Personal Details")

    email = st.text_input("Email", "john.doe@example.com")
    address = st.text_input("Address", "123 Main St, Anytown, USA")
    shares = st.number_input("Number of shares", 100)
    age = st.number_input("Age", 30)

    st.write(f"Email: {email}")
    st.write(f"Address: {address}")
    st.write(f"Number of Shares: {shares}")
    st.write(f"Age: {age}")

def map_page():

        # Title
    st.title("Map of Sydney")

    map_data = pd.DataFrame({
        'lat': [-33.8688],
        'lon': [151.2093]
    })

    st.map(map_data)

def GPT_page():

    openai.api_key = st.secrets['openai_api_key']

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
        input_text = st.text_area('Enter your query or  exit with :q')
        submit_button = st.form_submit_button('Submit')

    # Process the input text when the button is clicked
    user_query = ""
    if submit_button:
        user_query = input_text

    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query, out_token)
        return st.write(f"{user_query} {response}")

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
    # Pages
    PAGES = {
        "Home": home_page,
        "Map": map_page,
        "ChatGPT" : GPT_page
    }

    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

main()
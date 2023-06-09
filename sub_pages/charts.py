import streamlit as st
import plotly.express as px
import pandas as pd
import st_pages as stp


def authenticated():

    # Title and icon
    stp.add_page_title()

    # Section 1 - Line Chart
    st.header("Section 1: Line Chart")

    # Assume we have some time series data
    df_line = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=100),
        'value': (pd.Series(range(100)) + pd.Series(range(100)).cumsum()).tolist()
    })

    fig1 = px.line(df_line, x='date', y='value', labels={'value': 'Values Over Time'})
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

    st.markdown(f'<a href="https://streamlit.io">https://streamlit.io</a>', unsafe_allow_html=True)


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

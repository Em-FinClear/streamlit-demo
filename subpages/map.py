import streamlit as st
import pandas as pd


def app():

    page = 'map'
    st.title(f'{st.session_state.app.pages[page].icon} {st.session_state.app.pages[page].title}')

    map_data = pd.DataFrame({
        'lat': [-33.8688],
        'lon': [151.2093]
    })

    st.map(map_data)
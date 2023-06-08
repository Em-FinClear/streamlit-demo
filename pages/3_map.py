import streamlit as st
import pandas as pd

def main():

    st.set_page_config(page_title="Map", page_icon="🗺️")

        # Title
    st.title("Map of Sydney")

    map_data = pd.DataFrame({
        'lat': [-33.8688],
        'lon': [151.2093]
    })

    st.map(map_data)

# main()
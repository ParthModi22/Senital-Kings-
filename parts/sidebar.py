import streamlit as st

def sidebar_navigation():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["Irrigation Monitoring", "Maps Visualization", "Vegetation Indices"]
    )
    return page

import streamlit as st

def sidebar_navigation():
    # Create a sidebar with page options
    st.sidebar.title("Navigation")
    # Create selectbox for page navigation
    page = st.sidebar.selectbox("Select a page", ["Irrigation Monitoring", "Maps Visualization", "Vegetation Indices"])
    return page

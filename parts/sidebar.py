import streamlit as st

def sidebar_navigation():
    st.sidebar.title("Navigation")
    # Create sidebar navigation options
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["Irrigation Monitoring", "Farm Maps", "Vegetation Indices"]  # Unified Farm Maps section
    )
    return page

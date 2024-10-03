import streamlit as st

def sidebar_navigation():
    
    col1, col2, col3 = st.sidebar.columns([1,8,1])
    with col1:
        st.write("")
    with col2:
        st.image('statics/images.jpeg',  use_column_width=True)
    with col3:
        st.write("")
    st.sidebar.markdown(
        "<div style='text-align: center; font-size:24px; font-weight:bold;'>SENTINAL KINGS</div>",
        unsafe_allow_html=True
    )
    st.sidebar.title("Navigation")
    # Create sidebar navigation options
    page = st.sidebar.selectbox(
        "Choose a section:",
        ["Irrigation Monitoring", "Farm Maps", "Vegetation Indices"]  # Unified Farm Maps section
    )
    return page

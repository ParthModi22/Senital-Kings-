import streamlit as st

# Load CSS file to apply styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the custom CSS file
local_css("styles.css")

# Sidebar Navigation
from sidebar import sidebar_navigation
from irrigation import irrigation_monitoring
from maps import maps_visualization
from vegetation import vegetation_indices

def main():
    # Use sidebar to navigate between different pages
    page = sidebar_navigation()

    # Render the appropriate page based on the selection
    if page == "Irrigation Monitoring":
        irrigation_monitoring()
    elif page == "Maps Visualization":
        maps_visualization()
    elif page == "Vegetation Indices":
        vegetation_indices()

if __name__ == "__main__":
    main()

import streamlit as st
from parts.sidebar import sidebar_navigation
from parts.irrigation import irrigation_monitoring
from parts.maps import maps_visualization
from parts.vegetation import vegetation_indices

# Load custom CSS file to style the app
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file for custom styling
local_css("styles.css")

# Main function to handle page rendering
def main():
    # Get the selected page from sidebar navigation
    page = sidebar_navigation()

    # Render the appropriate page based on selection
    if page == "Irrigation Monitoring":
        irrigation_monitoring()
    elif page == "Farm Maps":
        maps_visualization()  # Unified map visualization page
    elif page == "Vegetation Indices":
        vegetation_indices()

# Run the app
if __name__ == "__main__":
    main()

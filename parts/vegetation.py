import streamlit as st
from utils.utils import get_vegetation_index

def vegetation_indices():
    st.title("🌿 Vegetation Indices Monitoring")
    st.write("Analyze the vegetation health of your farm area based on selected indices like NDVI or EVI.")

    # Check if coordinates are already selected in session state from the map section
    if 'latitude' in st.session_state and 'longitude' in st.session_state:
        latitude = st.session_state['latitude']
        longitude = st.session_state['longitude']
        st.write(f"**Selected Location**: Latitude = {latitude:.4f}, Longitude = {longitude:.4f}")
    else:
        st.warning("Please select your farm location from the 'Farm Maps' section.")
        return

    # Display NDVI or other vegetation index for the selected location
    veg_index = get_vegetation_index(latitude, longitude)
    st.markdown(f"""
        <div style="background-color:#eaf4f9;padding:15px;border-radius:10px;">
            <h3 style="color:#2a4d69;">🌿 Vegetation Index (NDVI): {veg_index:.2f}</h3>
        </div>
    """, unsafe_allow_html=True)

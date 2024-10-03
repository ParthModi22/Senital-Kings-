import streamlit as st
from utlis import get_vegetation_index

def vegetation_indices():
    st.title("Vegetation Indices")
    st.write("This section provides an overview of vegetation indices such as NDVI and EVI for crop health assessment.")

    latitude = st.number_input("Latitude for Vegetation Indices", value=28.6139, format="%.4f")
    longitude = st.number_input("Longitude for Vegetation Indices", value=77.2090, format="%.4f")

    # Placeholder to show a calculated vegetation index
    veg_index = get_vegetation_index(latitude, longitude)
    st.write(f"### Vegetation Index (NDVI/NDRE): {veg_index:.2f}")

import streamlit as st
import folium
from streamlit_folium import st_folium

def maps_visualization():
    st.title("📍 Maps Visualization")
    st.markdown("""
        <div style="background-color:#f5f5f5;padding:10px;border-radius:10px;">
            <p>This section visualizes the farm area, showing irrigation needs and other relevant information on an interactive map.</p>
        </div>
    """, unsafe_allow_html=True)

    latitude = st.number_input("Latitude for Map", value=28.6139, format="%.4f")
    longitude = st.number_input("Longitude for Map", value=77.2090, format="%.4f")
    
    # Display map with folium
    map_display = show_map(latitude, longitude, 2.6)  # Example: irrigation requirement of 2.6 mm/day
    st_folium(map_display, width=700, height=500)

def show_map(lat, lon, ir):
    # Create a folium map centered on the given latitude and longitude
    map_ = folium.Map(location=[lat, lon], zoom_start=12)
    # Add a marker to indicate the location
    folium.Marker([lat, lon], popup=f"Irrigation Requirement: {ir:.2f} mm/day").add_to(map_)
    return map_

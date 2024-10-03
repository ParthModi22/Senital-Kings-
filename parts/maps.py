import streamlit as st
import folium
from streamlit_folium import st_folium

# Interactive map visualization
def maps_visualization():
    st.title("📍 Interactive Maps Visualization")
    st.write("Use the interactive map below to pinpoint your farm location.")

    # Default coordinates for map center (can be changed)
    initial_lat, initial_lon = 28.6139, 77.2090

    # Create a folium map centered at the initial coordinates
    map_ = folium.Map(location=[initial_lat, initial_lon], zoom_start=5)

    # Add an instruction to guide the farmer
    st.markdown("""
    **Instructions**: 
    - Click on the map to select your farm location.
    - The latitude and longitude will be displayed below the map.
    - You can use these coordinates for further calculations.
    """)

    # Add a click event to capture coordinates
    map_.add_child(folium.LatLngPopup())

    # Display the map
    map_data = st_folium(map_, width=700, height=500)

    # If the user clicked on the map, retrieve the coordinates
    if map_data and map_data['last_clicked']:
        latitude = map_data['last_clicked']['lat']
        longitude = map_data['last_clicked']['lng']
        st.write(f"**Selected Location**: Latitude = {latitude:.4f}, Longitude = {longitude:.4f}")

        # Show coordinates for further use
        st.session_state['latitude'] = latitude
        st.session_state['longitude'] = longitude

        # Add a button to confirm location selection and go to the irrigation section
        if st.button("🔄 Use this Location for Irrigation Monitoring"):
            st.success(f"Location set: Latitude = {latitude:.4f}, Longitude = {longitude:.4f}")
            # Redirect to irrigation monitoring page or store this location for later use
    else:
        st.warning("Click on the map to select a location.")

import leafmap.foliumap as leafmap
import streamlit as st
import folium
from streamlit_folium import st_folium

def maps_visualization():
    st.title("🌍 Farm Maps Analysis")
    st.write("""
        This section provides farmers with comprehensive map analysis tools. Use the options below to switch between different map views to better understand your farm's characteristics.
    """)

    # Unified Map Selector: Radio button to switch between different map views
    map_type = st.radio(
        "Select Map View",
        ("Interactive Map for Location Selection", "Single Map View", "Split Map Comparison", "3D Terrain Map")
    )

    # Render the appropriate map view based on user selection
    if map_type == "Interactive Map for Location Selection":
        interactive_location_selection_map()
    elif map_type == "Single Map View":
        show_single_map()
    elif map_type == "Split Map Comparison":
        show_split_map()
    elif map_type == "3D Terrain Map":
        show_3d_map()

# Function to create an interactive map for selecting location
def interactive_location_selection_map():
    st.subheader("📍 Interactive Location Selection Map")
    st.write("Click on the map to select a location. The latitude and longitude of the selected location will be displayed below.")

    # Default location (center of the map)
    initial_lat, initial_lon = 38.7946, -106.5348

    # Create a folium-based map centered on the default location
    # m = leafmap.Map(center=[initial_lat, initial_lon], zoom=5)
        # Create a folium map centered on the default location
    map_ = folium.Map(location=[initial_lat, initial_lon], zoom_start=5)

    # Enable drawing tool (this method should be available in leafmap.foliumap)
    # m.add_draw_control()
    map_.add_child(folium.LatLngPopup())

    # Display the map in Streamlit
    # m.to_streamlit(width=700, height=500)
    # Create a folium map centered on the default location
    map_ = folium.Map(location=[initial_lat, initial_lon], zoom_start=5)
    
    # Add a click event to the map to capture latitude and longitude
    map_.add_child(folium.LatLngPopup())  # Enables click-to-get-coordinates feature

    # Display the map in Streamlit
    map_data = st_folium(map_, width=700, height=500)
    # Display the map
    # map_data = st_folium(map_, width=700, height=500)

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

    # # Retrieve selected lat/lon from session state (if available)
    # if st.session_state.get('last_clicked'):
    #     latitude = st.session_state['last_clicked']['lat']
    #     longitude = st.session_state['last_clicked']['lng']
    #     st.write(f"**Selected Location**: Latitude = {latitude:.4f}, Longitude = {longitude:.4f}")

    #     # Store the selected coordinates in session state for other sections
    #     st.session_state['latitude'] = latitude
    #     st.session_state['longitude'] = longitude

# Function to display a single map view (e.g., NDVI)
def show_single_map():
    st.subheader("Single Map View")
    st.write("Visualize a single dataset, such as NDVI or soil moisture.")

    # Create a single map centered on a location
    m = leafmap.Map(center=[38.7946, -106.5348], zoom=5, draw_control=False, measure_control=False)
    m.add_basemap("HYBRID")

    # Add a layer for NDVI (replace with an actual data source URL)
    ndvi_url = "https://example.com/ndvi_layer"  # Placeholder URL
    m.add_tile_layer(url=ndvi_url, name="NDVI", attribution="NDVI Data Source")

    # Display the map in Streamlit
    m.to_streamlit(width=800, height=600)

# Function to display a split map comparing two datasets
def show_split_map():
    st.subheader("Split Map Comparison View")
    st.write("Compare two datasets side by side, such as NDVI and soil moisture.")

    # Create a split map using leafmap
    m = leafmap.Map(center=[38.7946, -106.5348], zoom=5, draw_control=False, measure_control=False)
    m.add_basemap("HYBRID")

    # Add layers for NDVI and soil moisture (replace with actual URLs)
    ndvi_url = "https://example.com/ndvi_layer"  # Placeholder URL for NDVI
    soil_moisture_url = "https://example.com/moisture_layer"  # Placeholder URL for soil moisture

    # Create split map with NDVI on the left and soil moisture on the right
    m.split_map(left_layer=ndvi_url, right_layer=soil_moisture_url, name_left="NDVI", name_right="Soil Moisture")

    # Display the map in Streamlit
    m.to_streamlit(width=800, height=600)

# Function to display a 3D terrain map
def show_3d_map():
    st.subheader("3D Terrain Map View")
    st.write("Explore the terrain and elevation data of your farm area.")

    # Create a 3D map with a terrain layer
    m = leafmap.Map(center=[38.7946, -106.5348], zoom=5, draw_control=False, measure_control=False)
    m.add_basemap("ESRI")  # Add ESRI terrain basemap

    # Add a DEM (Digital Elevation Model) layer (replace with an actual DEM data source)
    dem_url = "https://example.com/dem_layer"  # Placeholder URL for DEM data
    m.add_tile_layer(url=dem_url, name="Digital Elevation Model", attribution="DEM Data Source")

    # Display the 3D map in Streamlit
    m.to_streamlit(width=800, height=600)

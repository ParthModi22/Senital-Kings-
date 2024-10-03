import streamlit as st
import folium
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
import requests

# Function to fetch soil moisture data for a given area (bounding box) using NASA SMAP API
def get_soil_moisture(lat_min, lon_min, lat_max, lon_max):
    """
    Fetches soil moisture data for a given bounding box area using the NASA SMAP API.
    This function assumes a bounding box defined by (lat_min, lon_min) to (lat_max, lon_max).
    """
    try:
        # Example API URL, replace with actual NASA SMAP API endpoint for soil moisture
        url = f"https://nasa-smap-api.com/soil_moisture?lat_min={lat_min}&lon_min={lon_min}&lat_max={lat_max}&lon_max={lon_max}"
        response = requests.get(url)
        data = response.json()

        # Extract soil moisture data (mocked structure for demonstration)
        soil_moisture_value = data.get("soil_moisture", 0.25)  # Replace with actual field from response
        return soil_moisture_value
    except Exception as e:
        print(f"Error fetching soil moisture data: {e}")
        return None

def maps_visualization():
    st.title("🌍 Farm Maps Analysis")
    st.write("""
        This section provides farmers with comprehensive map analysis tools. Use the options below to switch between different map views, including moisture levels and 3D terrain visualization.
    """)

    # Unified Map Selector: Radio button to switch between different map views
    map_type = st.radio(
        "Select Map View",
        ("Interactive Map for Location Selection", "Single Map View", "Split Map Comparison", "3D Terrain Map", "Soil Moisture Mapping")
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
    elif map_type == "Soil Moisture Mapping":
        show_soil_moisture_map()

# Function to create an interactive map for selecting location
def interactive_location_selection_map():
    st.subheader("📍 Interactive Location Selection Map")
    st.write("Click on the map to select a location. The latitude and longitude of the selected location will be displayed below.")

    # Default location (center of the map)
    initial_lat, initial_lon = 38.7946, -106.5348

    # Create a folium map centered on the default location
    map_ = folium.Map(location=[initial_lat, initial_lon], zoom_start=5)

    # Enable drawing tool for area selection
    draw = folium.plugins.Draw(export=True)
    map_.add_child(draw)
    map_.add_child(folium.LatLngPopup())

    # Display the map in Streamlit
    map_data = st_folium(map_, width=700, height=500)

    # If the user clicked on the map, retrieve the coordinates
    if map_data and map_data['last_clicked']:
        latitude = map_data['last_clicked']['lat']
        longitude = map_data['last_clicked']['lng']
        st.write(f"**Selected Location**: Latitude = {latitude:.4f}, Longitude = {longitude:.4f}")

        # Store selected coordinates in session state
        st.session_state['latitude'] = latitude
        st.session_state['longitude'] = longitude

# Function to display a single map view (e.g., NDVI)
def show_single_map():
    st.subheader("Single Map View")
    st.write("Visualize a single dataset, such as NDVI or soil moisture.")

    # Create a single map centered on a location
    m = leafmap.Map(center=[38.7946, -106.5348], zoom=5, draw_control=True, measure_control=True)
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

# Function to display a soil moisture map for the selected area
def show_soil_moisture_map():
    st.subheader("Soil Moisture Mapping")
    st.write("Visualize soil moisture levels of your farm area.")

    # Check if coordinates are available
    if 'latitude' not in st.session_state or 'longitude' not in st.session_state:
        st.warning("Please select your farm location from the 'Interactive Map for Location Selection' section.")
        return

    lat = st.session_state['latitude']
    lon = st.session_state['longitude']

    # Define a bounding box around the selected location for soil moisture mapping (e.g., a 1 km² area)
    lat_min, lon_min = lat - 0.005, lon - 0.005
    lat_max, lon_max = lat + 0.005, lon + 0.005

    # Fetch soil moisture data using the bounding box coordinates
    soil_moisture = get_soil_moisture(lat_min, lon_min, lat_max, lon_max)

    if soil_moisture is not None:
        st.write(f"**Soil Moisture Level**: {soil_moisture:.2f} m³/m³ (Volumetric Water Content)")

        # Create a folium map with the soil moisture overlay
        soil_map = folium.Map(location=[lat, lon], zoom_start=15)
        folium.Circle(
            location=[lat, lon],
            radius=500,  # Radius in meters
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.4,
            popup=f"Soil Moisture: {soil_moisture:.2f} m³/m³"
        ).add_to(soil_map)

        # Display the soil moisture map in Streamlit
        st_folium(soil_map, width=800, height=600)
    else:
        st.error("Could not fetch soil moisture data for the selected location.")

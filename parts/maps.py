import streamlit as st
import leafmap.foliumap as leafmap

def maps_visualization():
    st.title("🌍 Farm Maps Analysis")
    st.write("""
        This section provides farmers with comprehensive map analysis tools. Use the options below to switch between different map views to better understand your farm's characteristics.
    """)

    # Unified Map Selector: Radio button to switch between different map views
    map_type = st.radio(
        "Select Map View",
        ("Single Map View", "Split Map Comparison", "3D Terrain Map")
    )

    # Render the appropriate map view based on user selection
    if map_type == "Single Map View":
        show_single_map()
    elif map_type == "Split Map Comparison":
        show_split_map()
    elif map_type == "3D Terrain Map":
        show_3d_map()

# Function to display a single map with a specific layer (e.g., NDVI)
def show_single_map():
    st.subheader("Single Map View")
    st.write("Visualize a single dataset, such as NDVI or soil moisture, for your farm area.")

    # Create a single map
    m = leafmap.Map(center=[28.6139, 77.2090], zoom=5, draw_control=False, measure_control=False)
    m.add_basemap("HYBRID")

    # Add a layer for NDVI (replace with an actual data source URL)
    ndvi_url = "https://example.com/ndvi_layer"  # Placeholder URL
    m.add_tile_layer(url=ndvi_url, name="NDVI", attribution="NDVI Data Source")

    # Display the map in Streamlit
    m.to_streamlit(width=800, height=600)

# Function to display a split map comparing two datasets (e.g., NDVI and soil moisture)
def show_split_map():
    st.subheader("Split Map Comparison View")
    st.write("Compare two datasets side by side, such as NDVI and soil moisture.")

    # Create a split map with two datasets
    m = leafmap.Map(center=[28.6139, 77.2090], zoom=5, draw_control=False, measure_control=False)
    m.add_basemap("HYBRID")

    # Add layers to the left and right of the split map (replace with actual URLs)
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
    m = leafmap.Map(center=[28.6139, 77.2090], zoom=5, draw_control=False, measure_control=False)
    m.add_basemap("ESRI")

    # Add a DEM (Digital Elevation Model) layer (replace with an actual DEM data source)
    dem_url = "https://example.com/dem_layer"  # Placeholder URL for DEM data
    m.add_tile_layer(url=dem_url, name="Digital Elevation Model", attribution="DEM Data Source")

    # Display the 3D map in Streamlit
    m.to_streamlit(width=800, height=600)

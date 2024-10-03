import requests
import streamlit as st

# NASA POWER API - Reference ET Function
def get_reference_et(lat, lon):
    """
    Fetches the reference evapotranspiration (ET₀) data for a given latitude and longitude
    using the NASA POWER API.
    """
    try:
        url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&start=20230101&end=20230101&latitude={lat}&longitude={lon}&community=ag&format=json"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extract the ET₀ value from the response data
        et0_value = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']['20230101']
        return et0_value
    except Exception as e:
        st.error(f"Error fetching reference ET: {e}")
        return 5.5  # Default value in case of error

# MODIS or Alternative API for Actual ET
def get_actual_et(lat, lon):
    """
    Fetches the actual evapotranspiration (ET) data for a given location.
    This function uses a placeholder MODIS API, replace with the actual API endpoint.
    """
    try:
        # Replace with the actual MODIS API endpoint
        url = f"https://modis-api-placeholder.com/et?lat={lat}&lon={lon}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract the ET value (example parsing, update based on actual response structure)
        actual_et_value = data['et_value']
        return actual_et_value
    except Exception as e:
        st.error(f"Error fetching actual ET: {e}")
        return 4.0  # Default value in case of error

# Crop Coefficient (Kc) Data
def get_crop_coefficient(crop, stage):
    """
    Returns the crop coefficient (Kc) based on the crop type and growth stage.
    """
    kc_values = {
        "Maize": {"Initial": 0.3, "Development": 0.7, "Mid-season": 1.2, "Late-season": 0.5},
        "Wheat": {"Initial": 0.35, "Development": 0.75, "Mid-season": 1.15, "Late-season": 0.45},
        "Rice": {"Initial": 0.4, "Development": 0.8, "Mid-season": 1.3, "Late-season": 0.6},
    }
    return kc_values[crop][stage]

# Calculate Crop Water Requirement (CWR)
def calculate_cwr(et0, kc):
    """
    Calculate Crop Water Requirement (CWR) based on reference ET₀ and crop coefficient (Kc).
    """
    return et0 * kc

# Calculate Irrigation Requirement (IR)
def calculate_ir(cwr, actual_et):
    """
    Calculate Irrigation Requirement (IR) based on Crop Water Requirement (CWR) and actual ET.
    """
    return cwr - actual_et

# Vegetation Index (e.g., NDVI) Data from Sentinel Hub or Google Earth Engine
def get_vegetation_index(lat, lon):
    """
    Fetches the NDVI or other vegetation index data for a given location.
    Replace this with an actual API call, such as from Sentinel Hub or Google Earth Engine.
    """
    try:
        # Example Sentinel Hub or Google Earth Engine API URL (replace with actual endpoint)
        url = f"https://sentinelhub-api.com/ndvi?lat={lat}&lon={lon}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract NDVI value (update based on response structure)
        ndvi_value = data.get('ndvi_value', 0.65)  # Replace with actual key
        return ndvi_value
    except Exception as e:
        st.error(f"Error fetching NDVI data: {e}")
        return 0.65  # Default NDVI value in case of error

# Soil Moisture Data from OpenWeatherMap or Other API
def get_soil_moisture(lat, lon):
    """
    Fetches the soil moisture data for a given location using a third-party API.
    """
    try:
        # Example API URL (replace with OpenWeatherMap or SMAP API endpoint)
        api_key = "YOUR_API_KEY"
        url = f"https://api.openweathermap.org/data/2.5/soil_moisture?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract soil moisture value
        moisture_value = data.get('moisture', 0.3)  # Replace with actual key
        return moisture_value
    except Exception as e:
        st.error(f"Error fetching soil moisture data: {e}")
        return None

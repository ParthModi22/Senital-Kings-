import requests

# Function to get reference ET (ET₀) from NASA POWER API
def get_reference_et(lat, lon):
    """
    Fetches the reference evapotranspiration (ET₀) data for a given latitude and longitude
    using the NASA POWER API.
    """
    try:
        # NASA POWER API URL for reference ET₀ (Daily average)
        url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&start=20230101&end=20230101&latitude={lat}&longitude={lon}&community=ag&format=json"
        response = requests.get(url)
        data = response.json()
        
        # Extract the ET₀ value from the response data
        et0_value = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']['20230101']
        return et0_value
    except Exception as e:
        print(f"Error fetching reference ET: {e}")
        return 5.5  # Default value in case of error

# Function to get actual ET (ET) from MODIS data
def get_actual_et(lat, lon):
    """
    Fetches the actual evapotranspiration (ET) data from the MODIS satellite for a given location.
    """
    try:
        # Example URL structure, replace with actual MODIS API or data source if available
        # Note: You might need authentication or special API calls for real MODIS data
        url = f"https://modis-api-placeholder.com/et?lat={lat}&lon={lon}"
        response = requests.get(url)
        data = response.json()
        
        # Extract the ET value (example parsing, update based on actual response structure)
        actual_et_value = data['et_value']
        return actual_et_value
    except Exception as e:
        print(f"Error fetching actual ET: {e}")
        return 4.0  # Default value in case of error

# Function to get crop coefficient (Kc) based on crop type and growth stage
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

# Function to calculate Crop Water Requirement (CWR)
def calculate_cwr(et0, kc):
    """
    Calculate Crop Water Requirement (CWR) based on reference ET₀ and crop coefficient (Kc).
    """
    return et0 * kc

# Function to calculate Irrigation Requirement (IR)
def calculate_ir(cwr, actual_et):
    """
    Calculate Irrigation Requirement (IR) based on Crop Water Requirement (CWR) and actual ET.
    """
    return cwr - actual_et

# Function to fetch vegetation index (e.g., NDVI) for the given location
def get_vegetation_index(lat, lon):
    """
    Placeholder function for fetching vegetation index data (e.g., NDVI).
    Replace this with actual API calls or data source integration as needed.
    """
    return 0.65  # Mocked NDVI value for demo

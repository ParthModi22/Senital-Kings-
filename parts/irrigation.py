import streamlit as st
from utils.utils import get_reference_et, get_actual_et, get_crop_coefficient, calculate_cwr, calculate_ir

def irrigation_monitoring():
    st.title("🌿 Irrigation Requirement Monitoring")
    
    # Check if coordinates are already selected in the session state
    if 'latitude' in st.session_state and 'longitude' in st.session_state:
        latitude = st.session_state['latitude']
        longitude = st.session_state['longitude']
        st.write(f"**Selected Location**: Latitude = {latitude:.4f}, Longitude = {longitude:.4f}")
    else:
        st.warning("Please select your farm location from the 'Maps Visualization' section.")
        return

    # Input fields for the irrigation monitoring
    crop_type = st.selectbox("Select Crop Type", ["Maize", "Wheat", "Rice"])
    growth_stage = st.selectbox("Select Growth Stage", ["Initial", "Development", "Mid-season", "Late-season"])
    area = st.number_input("Area (in hectares)", value=1.0)

    # Add a button to perform irrigation requirement calculations
    if st.button("🚰 Get Irrigation Requirement"):
        # Calculate and display irrigation requirements
        et0 = get_reference_et(latitude, longitude)
        actual_et = get_actual_et(latitude, longitude)
        kc = get_crop_coefficient(crop_type, growth_stage)
        cwr = calculate_cwr(et0, kc)
        ir = calculate_ir(cwr, actual_et)
        
        # Styled output section
        st.markdown(f"""
            <div style="background-color:#eaf4f9;padding:15px;border-radius:10px;">
                <h3 style="color:#2a4d69;">💧 Crop Water Requirement (CWR): {cwr:.2f} mm/day</h3>
                <h3 style="color:#4caf50;">💦 Irrigation Requirement (IR): {ir:.2f} mm/day</h3>
            </div>
        """, unsafe_allow_html=True)


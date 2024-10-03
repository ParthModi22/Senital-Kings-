import streamlit as st
from utlis import get_reference_et, get_actual_et, get_crop_coefficient, calculate_cwr, calculate_ir

def irrigation_monitoring():
    st.title("🌿 Irrigation Requirement Monitoring")
    st.markdown("""
        <div style="background-color:#f9f9f9;padding:10px;border-radius:10px;margin-bottom:20px;">
            <p>This section provides insights on the irrigation requirements for different crops based on their growth stage and location.</p>
        </div>
    """, unsafe_allow_html=True)

    # Input fields for the irrigation monitoring
    crop_type = st.selectbox("Select Crop Type", ["Maize", "Wheat", "Rice"])
    growth_stage = st.selectbox("Select Growth Stage", ["Initial", "Development", "Mid-season", "Late-season"])
    latitude = st.number_input("Latitude", value=28.6139, format="%.4f")
    longitude = st.number_input("Longitude", value=77.2090, format="%.4f")
    area = st.number_input("Area (in hectares)", value=1.0)

    # Adding some styling to the button
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

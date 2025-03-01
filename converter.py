# Project 01: Unit Converter using Python and Streamlit

import streamlit as st

# CSS Styling
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e2f;
            color: white;
        }
        .stApp {
            background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        }
        h1 { 
            text-align: center;
            font-size: 36px;
            color: white;
        }
        .stButton>button {
            background: linear-gradient(45deg, #0b5394, #351c75);
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0px 5px rgba(0, 201, 255, 0.4);
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #92fe9d, #00c9ff);
            color: black;
        }
        .result-box {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            background: rgba(255, 255, 255, 1);
            padding: 25px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

# Input for Value
value = st.number_input("Enter the value", value=0.0, min_value=0.0, step=0.1)

# Columns for selecting From and To units
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Miles", "Yards", "Feet", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Miles", "Yards", "Feet", "Inches"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def convert_length(from_unit, to_unit, value):
    length_units = {
        "Meters": 1.0, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Micrometers": 1e6, 
        "Nanometers": 1e9, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    }
    return value / length_units[from_unit] * length_units[to_unit]

def convert_weight(from_unit, to_unit, value):
    weight_units = {
        "Kilograms": 1.0, "Grams": 1000, "Milligrams": 1e6, "Micrograms": 1e9, "Pounds": 2.20462, "Ounces": 35.274
    }
    return value / weight_units[from_unit] * weight_units[to_unit]

def convert_temperature(from_unit, to_unit, value):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Button to Trigger Conversion
if st.button("☠ Convert"):
    if conversion_type == "Length":
        result = convert_length(from_unit, to_unit, value)
    elif conversion_type == "Weight":
        result = convert_weight(from_unit, to_unit, value)
    elif conversion_type == "Temperature":
        result = convert_temperature(from_unit, to_unit, value)

    # Display Result
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Created with Hard Work by Sheeraz Ahmed Jogi</div>", unsafe_allow_html=True)
    
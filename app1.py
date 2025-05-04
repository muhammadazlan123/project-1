import streamlit as st

# Function to perform the unit conversion
def convert_units():
    # Title of the app
    st.title("Unit Converter")

    # Select the category of conversion
    category = st.selectbox("Select the type of conversion", ["Length", "Weight", "Temperature"])

    if category == "Length":
        unit = st.selectbox("Convert from (m/km/cm)", ["m", "km", "cm"])
        value = st.number_input("Enter value:", min_value=0.0)
        
        if unit == "m":
            st.write(f"{value} meters = {value / 1000} kilometers, {value * 100} centimeters")
        elif unit == "km":
            st.write(f"{value} kilometers = {value * 1000} meters, {value * 100000} centimeters")
        elif unit == "cm":
            st.write(f"{value} centimeters = {value / 100} meters, {value / 100000} kilometers")
    
    elif category == "Weight":
        unit = st.selectbox("Convert from (kg/g/lb)", ["kg", "g", "lb"])
        value = st.number_input("Enter value:", min_value=0.0)
        
        if unit == "kg":
            st.write(f"{value} kilograms = {value * 1000} grams, {value * 2.20462} pounds")
        elif unit == "g":
            st.write(f"{value} grams = {value / 1000} kilograms, {value / 453.592} pounds")
        elif unit == "lb":
            st.write(f"{value} pounds = {value / 2.20462} kilograms, {value * 453.592} grams")
    
    elif category == "Temperature":
        unit = st.selectbox("Convert from (C/F/K)", ["C", "F", "K"])
        value = st.number_input("Enter value:", min_value=-273.15)  # For temperature, min can't be below absolute zero
        
        if unit == "C":
            st.write(f"{value} Celsius = {(value * 9/5) + 32} Fahrenheit, {value + 273.15} Kelvin")
        elif unit == "F":
            st.write(f"{value} Fahrenheit = {(value - 32) * 5/9} Celsius, {(value + 459.67) * 5/9} Kelvin")
        elif unit == "K":
            st.write(f"{value} Kelvin = {value - 273.15} Celsius, {(value - 273.15) * 9/5 + 32} Fahrenheit")
    

# Run the unit converter
if __name__ == "__main__":
    convert_units()

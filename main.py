import streamlit as st

st.title(" 🌎Unit Converter App 📏")
st.markdown("### This app converts units of length, Weight and Time Instantly! 🚀")
st.write("Welcome! Please select the type of conversion you would like to perform")

category = st.selectbox("Select a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462 
        
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    
    # Default return statement if no condition is met
    return 0

if category == "Length":
    unit = st.selectbox("📏 Select a unit", ["Miles to Kilometers", "Kilometers to Miles"])
    
elif category == "Weight":
    unit = st.selectbox("⚖️ Select a unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
    
elif category == "Time":
    unit = st.selectbox("⏰ Select a unit", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
    
value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result != 0:  # Check if the result is valid
        st.success(f"The result is {result:.2f}")  # Displaying the result up to 2 decimal places
    else:
        st.error("Invalid conversion selected. Please check your inputs.")
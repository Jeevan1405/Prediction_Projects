import pandas as pd
import pickle as pk
import streamlit as st
import base64

# Function to add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png" if image_file.name.endswith(".png") else "jpeg"};base64,{encoded_string});
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Call the function to add your background image
# Replace 'your_background_image.jpg' with the actual name of your image file
add_bg_from_local('background_image.png') # Make sure this file is in the same directory

# Rest of your Streamlit app code
# Load the model
try:
    model = pk.load(open('Model\Bengaluru_House_Price_model.pkl','rb'))
except FileNotFoundError:
    st.error("Error: Model file 'Bengaluru_House_Price_model.pkl' not found. Please make sure it's in the correct directory.")
    st.stop()

st.header("Bengaluru House Price Predictor")

# Load the data
try:
    data = pd.read_csv('Data\Cleaned_data.csv')
except FileNotFoundError:
    st.error("Error: Data file 'Cleaned.csv' not found. Please make sure it's in the correct directory.")
    st.stop()

if 'location' in data.columns:
    unique_locations = data['location'].unique()
    loc = st.selectbox('Choose the Location', unique_locations)
else:
    st.error("Error: 'location' column not found in 'Cleaned.csv'.")
    st.stop()

sqft = st.number_input('Enter the Total Sqft', min_value=1.0, value=1000.0)
beds = st.number_input('Enter No of Bedrooms', min_value=0, value=2)
bath = st.number_input('Enter No of Bathrooms', min_value=0, value=2)
balc = st.number_input('Enter No of Balconies', min_value=0, value=1)

input_data = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                          columns=['location', 'total_sqft', 'bath', 'balcony', 'bedroom'])

if st.button("Predict Price"):
    try:
        output = model.predict(input_data)
        predicted_price_lakhs = output[0]
        predicted_price_crores = predicted_price_lakhs / 100
        final_price = output[0] * 100000

        st.success(f'The estimated price of the house is ₹{final_price:,.2f}')
        st.info("Price displayed in Indian Rupees.")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.warning("Please check if the model expects one-hot encoded 'location' or if the input feature order is correct.")
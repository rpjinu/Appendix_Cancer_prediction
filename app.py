import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load saved LabelEncoders and ML Model
encoders = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\project_vs\appendix_predict\encoder.pkl")  # Dictionary of LabelEncoders
model = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\project_vs\appendix_predict\model.pkl")  # Trained ML Model

# Extract classes dynamically from the encoders
encoder_classes = {col: list(encoders[col].classes_) for col in encoders}

# Function to encode user input
def encode_input(user_input, encoders):
    encoded_data = {}
    for col, value in user_input.items():
        if col in encoders:  # Encode categorical features
            encoder = encoders[col]
            encoded_data[col] = encoder.transform([value])[0]  # Convert category to number
        else:
            encoded_data[col] = value  # Keep numerical data as is
    return encoded_data

# Streamlit UI
st.title("Appendix Cancer Prediction API")
st.write("Enter the details below to predict appendix cancer.")

# Collect user inputs dynamically
user_input = {}
for col, classes in encoder_classes.items():
    user_input[col] = st.selectbox(f"Select {col}:", classes)  # Dropdown for categorical features

# Predict button
if st.button("Predict"):
    # Encode inputs
    encoded_input = encode_input(user_input, encoders)

    # Convert to DataFrame (ensure column order matches model training)
    input_df = pd.DataFrame([encoded_input])

    # Assuming input_data is a dictionary from user input
    input_data = np.array(list(input_df.values())).reshape(1, -1)  # Convert to 2D array
    prediction = model.predict(input_data)[0]

    # Display result
    result = "Cancer Detected" if prediction == 1 else "No Cancer"
    st.success(f"Prediction: **{result}**")


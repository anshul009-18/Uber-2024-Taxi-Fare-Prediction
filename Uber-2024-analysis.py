import streamlit as st
import pickle as pkl
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler

# Load the trained model
with open("C:/Users/anshu/Anaconda/Uber/uber2024.sav", "rb") as model_file:
    model = pkl.load(model_file)

# Create a dummy dataset with correct feature structure for fitting the scaler
dummy_data = pd.DataFrame([[1, 12, 3, 0, 10, 20, 2.5, 0.5]], 
                          columns=['trip_distance', 'pickup_hour', 'pickup_day', 'is_weekend',
                                   'trip_duration', 'average_speed', 'fare_per_mile', 'fare_per_minute'])

# Initialize and fit the scaler
scaler = StandardScaler()
scaler.fit(dummy_data)  # Ensures the scaler is ready for use

# Streamlit UI
st.title("🚖 Taxi Fare Prediction App")
st.markdown("### Enter the trip details below to predict the fare:")

# User inputs
trip_distance = st.number_input("Trip Distance (miles)", min_value=0.1, step=0.1)
pickup_hour = st.number_input("Pickup Hour (0-23)", min_value=0, max_value=23, step=1)
pickup_day = st.selectbox("Pickup Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
is_weekend = 1 if pickup_day in ["Saturday", "Sunday"] else 0
trip_duration = st.number_input("Trip Duration (minutes)", min_value=1, step=1)
average_speed = st.number_input("Average Speed (mph)", min_value=1, step=1)
fare_per_mile = st.number_input("Fare Per Mile", min_value=1.0, step=0.1)
fare_per_minute = st.number_input("Fare Per Minute", min_value=0.1, step=0.1)

# Convert pickup_day to numerical value (0=Monday, 6=Sunday)
pickup_day_num = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(pickup_day)

# Predict button
if st.button("Predict Fare 💰"):
    # Create a DataFrame for input data
    input_data = pd.DataFrame([[trip_distance, pickup_hour, pickup_day_num, is_weekend,
                                trip_duration, average_speed, fare_per_mile, fare_per_minute]],
                              columns=['trip_distance', 'pickup_hour', 'pickup_day', 'is_weekend',
                                       'trip_duration', 'average_speed', 'fare_per_mile', 'fare_per_minute'])

    # Transform input data using the fitted scaler
    input_data_scaled = scaler.transform(input_data)

    # Predict using the trained model
    prediction = model.predict(input_data_scaled)

    # Display prediction
    st.success(f"💲 Predicted Fare: ${prediction[0]:.2f}")

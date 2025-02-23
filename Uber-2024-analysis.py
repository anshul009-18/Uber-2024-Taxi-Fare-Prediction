import streamlit as st
import pickle as pkl
import pandas as pd
from sklearn.preprocessing import StandardScaler

with open("C:/Users/anshu/Anaconda/Uber/uber2024.sav", "rb") as model_file:
    model = pkl.load(model_file)

dummy_data = pd.DataFrame([[1, 12, 3, 0, 10, 20, 2.5, 0.5]], 
                          columns=['trip_distance', 'pickup_hour', 'pickup_day', 'is_weekend',
                                   'trip_duration', 'average_speed', 'fare_per_mile', 'fare_per_minute'])

scaler = StandardScaler()
scaler.fit(dummy_data)

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

pickup_day_num = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(pickup_day)

# Predict button
if st.button("Predict Fare 💰"):
    input_data = pd.DataFrame([[trip_distance, pickup_hour, pickup_day_num, is_weekend,
                                trip_duration, average_speed, fare_per_mile, fare_per_minute]],
                              columns=['trip_distance', 'pickup_hour', 'pickup_day', 'is_weekend',
                                       'trip_duration', 'average_speed', 'fare_per_mile', 'fare_per_minute'])

    input_data_scaled = scaler.transform(input_data)

    prediction = model.predict(input_data_scaled)

    st.success(f"💲 Predicted Fare: ${prediction[0]:.2f}")

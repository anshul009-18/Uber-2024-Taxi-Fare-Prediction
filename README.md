# 🚖 Uber 2024 Taxi Fare Prediction

## 📌 Project Overview
This project is a **taxi fare prediction web app** built using **Streamlit** and a **pre-trained machine learning model**. Users can input trip details, and the app predicts the estimated fare using a trained model. This project aims to provide a user-friendly interface for quickly estimating ride fares based on historical trip data.

## 🔎 What is Happening in This Project?
1. **User Inputs Trip Details**: Users provide trip-related information such as distance, pickup time, and speed.
2. **Preprocessing & Feature Scaling**: The app processes inputs and applies `StandardScaler` to normalize data.
3. **Model Prediction**: A pre-trained machine learning model (`uber2024.sav`) predicts the fare based on input features.
4. **Displaying Results**: The estimated fare is displayed instantly in the Streamlit UI.
5. **Continuous Improvements**: The model can be enhanced with additional features like traffic, weather, and special events.

## 📊 Dataset & Model
- The dataset consists of Uber trip data, including:
  - **Trip Distance**: Total miles traveled.
  - **Pickup & Drop-off Time**: Timestamp of trip initiation and completion.
  - **Fare Components**: Base fare, tolls, surcharges, and tips.
  - **Passenger & Payment Information**: Number of passengers and payment type.
- The machine learning model (`uber2024.sav`) was trained using **StandardScaler** to normalize features before making predictions.
- The model takes structured input and provides an accurate fare estimate based on past data trends.

## ⚙️ Features
- **User-friendly Streamlit UI**: Simple and interactive interface for entering trip details.
- **Dynamic Fare Calculation**: Uses an ML model to predict fares based on real trip data.
- **Feature Scaling**: Ensures numerical inputs are correctly scaled before making predictions.
- **Interactive Prediction**: Users can get an instant fare estimate by entering trip details.
- **Automatic Weekend & Daytime Adjustments**: Recognizes weekend trips and time of day to refine predictions.

## 🛠️ Installation & Setup
### Prerequisites
Ensure you have Python installed and the required dependencies:
```bash
pip install streamlit pandas scikit-learn pickle-mixin
```

### Running the App
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Uber-Fare-Prediction.git
   cd Uber-Fare-Prediction
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run "Uber 2024 analysis.py"
   ```

## 🖥️ Usage
1. Enter the required trip details (distance, time, fare per mile, etc.).
2. Click the **Predict Fare 💰** button.
3. The app processes the data and displays the estimated fare instantly.

## 🔍 How It Works
- The app takes user inputs and processes them into a structured dataframe.
- The trained model, loaded from a `.sav` file, applies **StandardScaler** transformations to match the training dataset format.
- The model predicts the fare and returns an estimated trip cost to the user.

## 🚀 Future Improvements
- **Enhance the ML model** with more features such as:
  - Weather and traffic conditions
  - Special event surcharges
  - Time of day fare variations
- **Add visualization tools** to display fare trends and trip patterns.
- **Expand deployment options** to cloud services like Heroku or AWS Lambda for easier access.

## 📜 Data Source
The dataset used in this project is sourced from the NYC Taxi & Limousine Commission (TLC): [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). The dataset includes detailed trip records and fare breakdowns for extensive analysis.

## 🤝 Contributing
We welcome contributions! If you want to improve the model, UI, or add new features, feel free to:
- Fork the repository
- Open an issue for discussion
- Submit a pull request with your changes

Let's make taxi fare predictions smarter together! 🚕


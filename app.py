import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Train Journey Time Prediction",
    page_icon="🚆",
    layout="wide"
)


# ==========================================================
# LOAD MODEL AND DATA
# ==========================================================

model = joblib.load("improved_linear_regression_model.pkl")

train_journey = pd.read_csv("train_journey_cleaned.csv")


# ==========================================================
# PREPARE DATA FOR MODEL EVALUATION
# ==========================================================

X = train_journey[
    ["Total_Distance", "Number_of_Stops"]
]

y = train_journey["Journey_Duration"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# Generate predictions for test data
y_pred = model.predict(X_test)


# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)


# ==========================================================
# TITLE
# ==========================================================

st.title("🚆 Train Journey Time Prediction System")

st.write(
    "A Machine Learning-based application that predicts "
    "train journey duration using total distance and "
    "number of stops."
)


st.divider()


# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.subheader("📌 Project Overview")

st.write(
    "This project uses Machine Learning to estimate train "
    "journey duration from journey-related features. "
    "The final model uses Total Distance and Number of Stops "
    "as input features."
)


# ==========================================================
# USER INPUT
# ==========================================================

st.subheader("📥 Enter Journey Details")


col1, col2 = st.columns(2)


with col1:

    total_distance = st.number_input(
        "📍 Total Distance",
        min_value=0.0,
        value=500.0,
        step=1.0
    )


with col2:

    number_of_stops = st.number_input(
        "🚉 Number of Stops",
        min_value=0,
        value=15,
        step=1
    )


# ==========================================================
# PREDICTION
# ==========================================================

st.write("")


if st.button("🔮 Predict Journey Time", use_container_width=True):

    input_data = pd.DataFrame({
        "Total_Distance": [total_distance],
        "Number_of_Stops": [number_of_stops]
    })


    prediction = model.predict(input_data)[0]


    # Prevent negative display
    prediction = max(prediction, 0)


    hours = int(prediction // 60)

    minutes = int(prediction % 60)


    st.success(
        f"Predicted Journey Duration: {prediction:.2f} minutes"
    )


    st.info(
        f"⏱️ Approximately {hours} hours and {minutes} minutes"
    )


# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.divider()

st.subheader("📊 Model Performance")


metric1, metric2 = st.columns(2)


with metric1:

    st.metric(
        label="Mean Absolute Error (MAE)",
        value=f"{mae:.2f} minutes"
    )


with metric2:

    st.metric(
        label="Root Mean Squared Error (RMSE)",
        value=f"{rmse:.2f} minutes"
    )


st.write(
    "Lower MAE and RMSE values indicate smaller prediction errors."
)


# ==========================================================
# ACTUAL VS PREDICTED VISUALIZATION
# ==========================================================

st.subheader("📈 Actual vs Predicted Journey Duration")


fig, ax = plt.subplots(figsize=(10, 6))


ax.scatter(
    y_test,
    y_pred,
    alpha=0.5
)


# Reference line
minimum_value = min(
    y_test.min(),
    y_pred.min()
)

maximum_value = max(
    y_test.max(),
    y_pred.max()
)


ax.plot(
    [minimum_value, maximum_value],
    [minimum_value, maximum_value],
    linestyle="--"
)


ax.set_xlabel(
    "Actual Journey Duration (minutes)"
)

ax.set_ylabel(
    "Predicted Journey Duration (minutes)"
)

ax.set_title(
    "Actual vs Predicted Journey Duration"
)


st.pyplot(fig)


st.write(
    "Points closer to the diagonal reference line represent "
    "predictions that are closer to the actual journey duration."
)


# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.divider()

st.subheader("🧠 About the Machine Learning Model")


info_col1, info_col2, info_col3 = st.columns(3)


with info_col1:

    st.write("**Model**")

    st.write("Linear Regression")


with info_col2:

    st.write("**Input Features**")

    st.write("Total Distance")

    st.write("Number of Stops")


with info_col3:

    st.write("**Target**")

    st.write("Journey Duration")


# ==========================================================
# TECHNOLOGIES
# ==========================================================

st.subheader("🛠️ Technologies Used")


st.write(
    "Python • Pandas • NumPy • Scikit-learn • "
    "Matplotlib • Streamlit"
)


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "Machine Learning-Based Train Journey Time Prediction System"
)
train_journey = pd.read_csv("train_journey_cleaned.csv")
import matplotlib.pyplot as plt
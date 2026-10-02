<<<<<<< HEAD
# 🚆 Machine Learning-Based Train Journey Time Prediction System

## 📌 Project Overview

This project develops a Machine Learning system to predict train journey duration using train schedule and route data.

The final system uses:

- Total Distance
- Number of Stops

to predict the journey duration in minutes.

The project also includes an interactive Streamlit web application where users can enter journey details and receive a predicted journey time.

## 🎯 Objective

The main objective is to build a Machine Learning-based system that can estimate train journey duration from schedule and route information.

## 📊 Project Levels

### Level 1 – Data Understanding
- Loaded and explored the train journey dataset.
- Studied dataset structure and features.
- Identified relevant columns.

### Level 2 – Data Cleaning and Feature Creation
- Cleaned the dataset.
- Created train-level journey information.
- Calculated Total Distance.
- Calculated Number of Stops.
- Calculated Journey Duration.

### Level 3 – Exploratory Data Analysis
- Analyzed relationships between journey features.
- Created visualizations to understand the data.
- Studied distance, stops, and journey duration.

### Level 4 – Model Training
- Trained a Linear Regression model.
- Used Total Distance as a basic feature.
- Evaluated model predictions using MAE and RMSE.

### Level 5 – Model Comparison
Two Linear Regression models were compared.

The improved model uses:

- Total Distance
- Number of Stops

The improved model achieved:

- MAE: 152.21 minutes
- RMSE: 237.39 minutes

### Level 6 – Interactive ML Application
A Streamlit web application was developed.

Users can enter:

- Total Distance
- Number of Stops

The application provides:

- Predicted journey duration
- Prediction in hours and minutes
- MAE
- RMSE
- Actual vs Predicted visualization
- Machine Learning model information

## 🤖 Machine Learning Model

**Model:** Linear Regression

### Input Features

1. Total Distance
2. Number of Stops

### Target

Journey Duration

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Streamlit
- Jupyter Notebook

## 📁 Project Structure

```text
Train_Journey_Time_Prediction/
│
├── app.py
├── Dataset1.csv
├── train_journey_cleaned.csv
├── improved_linear_regression_model.pkl
├── linear_regression_model.pkl
├── level5_model_comparison.xls
├── requirements.txt
├── .gitignore
├── README.md
│
├── Level_1_Data_understanding.ipynb
├── Level_2_ Data_Cleaning.ipynb
├── Level_3_EDA.ipynb
├── Level_4_Model_Training.ipynb
└── Level_5_Model_Comparison.ipynb
=======
# Train-Journey-Time-Prediction
>>>>>>> e72502c547063aa484f7d76edae054d042ff6e14

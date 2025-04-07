![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)
![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202025-blueviolet)
[![Download Release](https://img.shields.io/github/v/release/ReNewTechSolutions/fuel_consumption_prediction_multiple_regression_model?label=Download%20Release)](https://github.com/ReNewTechSolutions/fuel_consumption_prediction_multiple_regression_model/releases/latest)

# Fuel Consumption Prediction - Multiple Regression Model

## 📌 Project Overview

This project uses a **Multiple Linear Regression Model** to predict **CO₂ emissions** based on:

- **Engine Size (`ENGINESIZE`)**
- **Fuel Consumption (`FUELCONSUMPTION_COMB_MPG`)**

It now includes **hyperparameter tuning** using Ridge Regression and GridSearchCV.

## 📂 Project Structure

fuel_consumption_prediction_multiple_regression_model/ │── README.md # Project documentation │── train_model.py # Model training script │── evaluate_model.py # Model evaluation script │── visualize_results.py # Visualization script │── hyperparameter_tuning.py # Ridge Regression hyperparameter tuning │── requirements.txt # Required dependencies

bash
Copy
Edit

## 📊 Dataset

- The dataset used for training is from **IBM Developer Skills Network**.
- It contains various vehicle attributes and their **CO₂ emissions**.

## 🚀 How to Run This Project

1️⃣ **Clone the repository**

```bash
git clone https://github.com/ReNewTechSolutions/fuel_consumption_prediction_multiple_regression_model.git
cd fuel_consumption_prediction_multiple_regression_model
2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the model training script

bash
Copy
Edit
python train_model.py
4️⃣ Evaluate model performance

bash
Copy
Edit
python evaluate_model.py
5️⃣ Visualize the results

bash
Copy
Edit
python visualize_results.py
6️⃣ Perform hyperparameter tuning

bash
Copy
Edit
python hyperparameter_tuning.py
📌 Model Performance Metrics
After training and tuning, the model is evaluated using:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

R² Score

📊 Visualization
The project generates a 3D regression plane for better interpretation.

Scatter plots help compare actual vs predicted emissions.

Ridge Regression tuning is performed and evaluated separately.

🛠 Future Improvements
Feature Engineering: Consider adding more vehicle parameters.

Polynomial Regression: Improve prediction accuracy.

Hyperparameter Tuning: Expand to Lasso and ElasticNet tuning.

Cross-Validation: Apply more robust evaluation strategies.

📝 Project Inspiration
This project was inspired by coursework from the IBM Developer Skills Network (Machine Learning with Python specialization).
The structure and initial dataset were based on a guided lab.
All code and enhancements (such as hyperparameter tuning and additional documentation) were independently developed.

📌 Author: Felicia Goad
📌 License: MIT
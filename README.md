# Fuel Consumption Prediction - Multiple Regression Model

## 📌 Project Overview

This project uses a **Multiple Linear Regression Model** to predict **CO2 emissions** based on:

- **Engine Size (********`ENGINESIZE`********\*\*\*\*)**
- **Fuel Consumption (********`FUELCONSUMPTION_COMB_MPG`********\*\*\*\*)**

## 📂 Project Structure

```
📁 fuel_consumption_prediction_multiple_regression_model
│── 📝 README.md           # Project documentation
│── 📝 train_model.py      # Model training script
│── 📝 evaluate_model.py   # Model evaluation script
│── 📝 visualize_results.py # Visualization script
│── 📝 requirements.txt    # Required dependencies
```

## 📊 Dataset

- The dataset used for training is from **IBM Developer Skills Network**.
- It contains various vehicle attributes and their **CO2 emissions**.

## 🚀 How to Run This Project

1️⃣ **Clone the repository**

```bash
git clone https://github.com/YourUsername/fuel_consumption_prediction_multiple_regression_model.git
cd fuel_consumption_prediction_multiple_regression_model
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Run the model training script**

```bash
python train_model.py
```

4️⃣ **Evaluate model performance**

```bash
python evaluate_model.py
```

5️⃣ **Visualize the results**

```bash
python visualize_results.py
```

## 📌 Model Performance Metrics

After training, the model is evaluated using:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

## 📊 Visualization

- The project generates a **3D regression plane** for better interpretation.
- Scatter plots help compare actual vs predicted emissions.

## 🛠 Future Improvements

- **Feature Engineering**: Consider adding more vehicle parameters.
- **Polynomial Regression**: Improve prediction accuracy.
- **Hyperparameter Tuning**: Optimize the model.

---

📌 **Author:** Felicia Goad\
📌 **License:** MIT

---

# Fuel Consumption Prediction - Multiple Regression Model

This project predicts CO2 emissions based on Engine Size and Fuel Consumption using Multiple Regression.


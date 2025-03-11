# Hyperspectral Imaging for Mycotoxin Prediction in Corn

## 📌 Project Overview

This project applies **machine learning and deep learning** techniques to analyze **hyperspectral imaging (HSI) data** for predicting **vomitoxin\_ppb** levels in corn samples. The dataset used is `task.csv`, and the goal is to develop an accurate regression model for mycotoxin level prediction.

## 💂️️ Dataset

- **task.csv**: Contains hyperspectral features and target variable (**vomitoxin\_ppb**).
- Features: Spectral bands from hyperspectral imaging.
- Target: **Vomitoxin\_ppb** (mycotoxin concentration in parts per billion).

## 📊 Exploratory Data Analysis (EDA)

- **Data Cleaning**: Checked for missing values and handled outliers.
- **Visualization**: Histograms, boxplots, and correlation heatmaps to understand feature distributions.
- **Outlier Detection & Handling**: Used IQR method and log transformations where necessary.
- **Dimensionality Reduction**:
  - Applied **Principal Component Analysis (PCA)** to reduce redundant features.
  - Used **t-SNE** for data visualization in lower dimensions.

## 🏰️ Models Implemented

Several machine learning and deep learning models were trained and compared:

1. **CNN (Convolutional Neural Network)** ✅
2. **LSTM (Long Short-Term Memory Network)** ✅
3. **Random Forest
4. **Linear regression
5. **Xgboost

## 📈 Experiment Tracking with MLflow

To systematically compare models, **MLflow** was used for:

- Logging **MAE, MSE, and R² scores**.
- Tracking hyperparameter tuning.
- Comparing models in an organized way.

Hyperspectral Imaging for Mycotoxin Prediction in Corn

📌 Project Overview

This project applies machine learning and deep learning techniques to analyze hyperspectral imaging (HSI) data for predicting vomitoxin_ppb levels in corn samples. The dataset used is task.csv, and the goal is to develop an accurate regression model for mycotoxin level prediction.

💂️️ Dataset

task.csv: Contains hyperspectral features and target variable (vomitoxin_ppb).

Features: Spectral bands from hyperspectral imaging.

Target: Vomitoxin_ppb (mycotoxin concentration in parts per billion).

📊 Exploratory Data Analysis (EDA)

Data Cleaning: Checked for missing values and handled outliers.

Visualization: Histograms, boxplots, and correlation heatmaps to understand feature distributions.

Outlier Detection & Handling: Used IQR method and log transformations where necessary.

Dimensionality Reduction:

Applied Principal Component Analysis (PCA) to reduce redundant features.

Used t-SNE for data visualization in lower dimensions.

🏰️ Models Implemented

Several machine learning and deep learning models were trained and compared:

CNN (Convolutional Neural Network) ✅

GNN (Graph Neural Network) ✅

LSTM (Long Short-Term Memory Network) ✅

Transformer-based Model ✅ (Time-Series Transformer adapted for hyperspectral data)

📈 Experiment Tracking with MLflow

To systematically compare models, MLflow was used for:

Logging MAE, MSE, and R² scores.

Tracking hyperparameter tuning.

Comparing models in an organized way.

🏆 Results & Model Comparison

Model

MAE

MSE

R² Score

CNN

1.91

6.63

0.18

GNN

🌊 Results pending





LSTM

🌊 Results pending





Transformer

🌊 Results pending





🔍 Conclusion: The best-performing model will be determined based on evaluation metrics.

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/your_username/hyperspectral-mycotoxin-prediction.git
cd hyperspectral-mycotoxin-prediction

Install dependencies:

pip install -r requirements.txt

Run the Jupyter Notebook for training models:

jupyter notebook

View MLflow experiment results:

mlflow ui

🔥 Future Enhancements

Attention Visualization for Transformer model.

Hyperparameter Tuning for performance improvements.

Deploy as a Streamlit Web App.

📌 Author: Your Name📌 Repository: GitHub Link
import streamlit as st
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestRegressor
 

scaler = joblib.load("scaler.pkl")  
selected_features = joblib.load("selected_features.pkl")  
best_rf_model = joblib.load("rf_model.pkl")


st.title("🌽 Hyperspectral Mycotoxin Prediction App")
st.write("Upload a dataset to predict **vomitoxin_ppb** levels in corn samples.")


uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file: 

    df = pd.read_csv(uploaded_file)
    
    missing_features = [col for col in selected_features if col not in df.columns]
    if missing_features:
        st.error(f"Missing features in uploaded file: {missing_features}")
    else:
      
        X_scaled = scaler.transform(df[selected_features])
        
     
        y_pred_log = best_rf_model.predict(X_scaled)
        y_pred = np.expm1(y_pred_log)  
        
      
        df["Predicted_vomitoxin_ppb"] = y_pred
        st.write("### Predictions")
        st.dataframe(df)

        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Download Predictions", data=csv, file_name="predictions.csv", mime="text/csv")

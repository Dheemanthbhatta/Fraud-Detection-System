import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('fraud_model.pkl')

st.set_page_config(page_title="Fraud Guard AI", page_icon="🛡️")

st.title("🛡️ Fraud Detection System")
st.write("This AI model analyzes 30 different behavioral features to detect fraudulent credit card activity.")

# Create a layout with columns
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)
    time = st.number_input("Seconds since last transaction", value=3600)

with col2:
    v1 = st.slider("Behavior Feature V1 (Anonymized)", -5.0, 5.0, 0.0)
    v2 = st.slider("Behavior Feature V2 (Anonymized)", -5.0, 5.0, 0.0)

# In a real scenario, we'd input all 28 V-features. 
# For this demo, we will pad the rest with zeros.
if st.button("Run Fraud Analysis"):
    # Create the input array (30 features total)
    features = np.zeros(30)
    features[0] = time
    features[1] = v1
    features[2] = v2
    features[29] = amount
    
    prediction = model.predict([features])[0]
    
    st.divider()
    if prediction > 0.5: # Or use your 'best_threshold'
        st.error(f"🚨 HIGH RISK DETECTED (Score: {prediction:.4f})")
        st.write("Action: Transaction Blocked. Alerting user via SMS.")
    else:
        st.success(f"✅ TRANSACTION SAFE (Score: {prediction:.4f})")
        st.write("Action: Transaction Approved.")
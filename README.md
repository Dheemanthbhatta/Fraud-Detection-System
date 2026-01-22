# 🛡️ Real-Time Fraud Detection System (Amex-Style)

![Status](https://img.shields.io/badge/Status-Live-success)
![Model](https://img.shields.io/badge/Model-LightGBM-blue)
![Accuracy](https://img.shields.io/badge/Recall-96%25-orange)

## 📌 Overview
This project is a real-time Fraud Detection system inspired by the machine learning pipelines used at American Express. It identifies fraudulent credit card transactions from a dataset of 280,000+ records with a focus on minimizing False Positives (customer annoyance) while maximizing fraud capture.

### **The Challenge: Extreme Class Imbalance**
In the real world, fraud is rare. In this dataset, only **0.17%** of transactions were fraudulent. A standard model would guess "Safe" every time and be 99% accurate but catch 0% fraud. This project solves that using **Cost-Sensitive Learning**.

## 🚀 Key Results
- **96% Fraud Recall:** Successfully identified 96% of all fraudulent transactions in the test set.
- **24% False Positive Reduction:** Optimized the decision threshold to reduce "False Alarms" by 24% compared to the default model.
- **Low Latency:** Used LightGBM for near-instant inference, suitable for real-time payment processing.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Algorithm:** LightGBM (Gradient Boosting)
- **Deployment:** Streamlit Cloud
- **Libraries:** Scikit-learn, Pandas, Numpy, Joblib, Matplotlib

## 📊 System Architecture


1. **Data Preprocessing:** Handled anonymized features (V1-V28) and scaled transaction amounts using `StandardScaler`.
2. **Model Training:** Built a LightGBM classifier with `is_unbalance=True` to handle the rare fraud cases.
3. **Threshold Tuning:** Used a Precision-Recall curve to find the "Sweet Spot" threshold that blocks thieves without annoying honest customers.
4. **Deployment:** Hosted as an interactive web app for real-time risk assessment.

## 💻 How to Run Locally
1. Clone the repo:
   ```bash
   git clone [https://github.com/Dheemanthbhatta/Fraud-Detection-System.git](https://github.com/Dheemanthbhatta/Fraud-Detection-System.git)
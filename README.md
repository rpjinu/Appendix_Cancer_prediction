# Appendix_Cancer_prediction
"This project builds an end-to-end Appendix Cancer Prediction system using machine learning, where categorical inputs are encoded, selected features are used for training a RandomForestClassifier, and a Streamlit API allows users to input data, which gets encoded, processed, and predicted in real time. 🚀"

# 🎗️ Appendix Cancer Prediction - End-to-End Machine Learning Project

## 📌 Project Overview  
This project aims to **predict appendix cancer** using **machine learning**.  
It includes **data preprocessing, feature selection, model training, and API deployment** via **Streamlit**.  

---

## 🛠️ Tech Stack  
- 🐍 **Python**  
- 📊 **Pandas, NumPy** – Data processing  
- 🎭 **Scikit-learn** – Machine Learning  
- 🌳 **Random Forest Classifier** – Model  
- 🔤 **Label Encoding** – Categorical feature transformation  
- 🎛️ **Feature Selection** – Optimizing input features  
- 🚀 **Streamlit** – API & UI Deployment  

---

## 🔄 Workflow  

1️⃣ **Data Preprocessing**  
   - Convert categorical features using **Label Encoding** 🔤  
   - Handle missing values and normalize data 📏  

2️⃣ **Feature Selection**  
   - Identify & drop less important features ❌  
   - Keep only the most relevant ones ✅  

3️⃣ **Model Training**  
   - Train a **RandomForestClassifier** 🌳  
   - Save the trained model & label encoders 💾  

4️⃣ **API Deployment**  
   - Build a **Streamlit app** for user input 🎛️  
   - Load the **encoder** to transform inputs 🔄  
   - Use the **ML model** to predict cancer risk 🎯  

---

## 🏗️ Installation & Setup  

```bash
# Clone the repository
git clone https://github.com/yourusername/appendix-cancer-prediction.git
cd appendix-cancer-prediction

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

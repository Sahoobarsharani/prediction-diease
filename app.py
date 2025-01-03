import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Disease Outbreak Prediction",
                   layout="wide",
                   page_icon="🩺")

# Load the models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        menu_icon="activity",
        icons=["droplet", "heart", "brain"],
        default_index=0,
    )

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 36px;
        text-align: center;
        margin-bottom: 20px;
        color: #2c3e50;
    }
    .sub-header {
        text-align: center;
        color: #34495e;
        margin-bottom: 40px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>Disease Outbreak Prediction System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Using Machine Learning Models by Barsha Rani Sahoo</div>", unsafe_allow_html=True)

# Function to display banners and inputs
def add_inputs(title, inputs):
    st.markdown(f"<h3 style='color:#2c3e50;'>{title}</h3>", unsafe_allow_html=True)
    return [st.text_input(label, "") for label in inputs]

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    user_inputs = add_inputs(
        "Diabetes Prediction using ML",
        ["Number of Pregnancies", "Glucose Level", "Blood Pressure Value", "Skin Thickness Value", 
         "Insulin Level", "BMI Value", "Diabetes Pedigree Function Value", "Age"]
    )

    if st.button("Diabetes Test Result"):
        try:
            prediction = diabetes_model.predict([[float(x) for x in user_inputs]])[0]
            diagnosis = "The person is diabetic" if prediction == 1 else "The person is not diabetic"
            st.success(diagnosis)
        except Exception as e:
            st.error(f"Error: {e}")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    user_inputs = add_inputs(
        "Heart Disease Prediction using ML",
        ["Age", "Sex", "Chest Pain Type", "Resting Blood Pressure", "Serum Cholesterol (mg/dl)", 
         "Fasting Blood Sugar (>120 mg/dl)", "Resting Electrocardiographic Results", 
         "Maximum Heart Rate Achieved", "Exercise Induced Angina", "ST Depression Induced by Exercise", 
         "Slope of Peak Exercise ST Segment", "Major Vessels Colored by Fluoroscopy", 
         "Thalassemia (0=Normal; 1=Fixed Defect; 2=Reversible Defect)"]
    )

    if st.button("Heart Disease Test Result"):
        try:
            prediction = heart_disease_model.predict([[float(x) for x in user_inputs]])[0]
            diagnosis = "The person has heart disease" if prediction == 1 else "The person does not have heart disease"
            st.success(diagnosis)
        except Exception as e:
            st.error(f"Error: {e}")

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    user_inputs = add_inputs(
        "Parkinson's Disease Prediction using ML",
        ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", 
         "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", 
         "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", "RPDE", 
         "DFA", "Spread1", "Spread2", "D2", "PPE"]
    )

    if st.button("Parkinson's Test Result"):
        try:
            prediction = parkinsons_model.predict([[float(x) for x in user_inputs]])[0]
            diagnosis = "The person has Parkinson's disease" if prediction == 1 else "The person does not have Parkinson's disease"
            st.success(diagnosis)
        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("""
    <footer style="text-align:center; margin-top:50px;">
        <p>Developed by <b>Barsha Rani Sahoo</b></p>
    </footer>
""", unsafe_allow_html=True)

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import base64

# Load the pre-trained model
with open('titanic_survivors_predictor.pkl', 'rb') as files:
    model, le_sex, le_embarked = pickle.load(files)

st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="centered")


#---- Adding Background Image ----
def add_bg_image(image_file):
    """Adds a background image to the Streamlit app."""
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stApp > header, .stApp > footer {{
            background-color: rgba(255, 255, 255, 0.5);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image("titanic-sinking.jpg") 
# App title and description
st.markdown("""
<style>
h1 {
    color: #2563EB;
}
.stButton>button {
    background-color: #2563EB;
    color: #ffffff;
    font-size: 16px;
    padding: 8px 16px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚢 Titanic Survival Predictor")
st.markdown("Enter details to predict if the passenger survived the Titanic disaster.")

#Inputs
col1, col2 = st.columns(2)

with col1:
    p_class = st.selectbox("Passenger Class (1 = Upper, 2 = Middle, 3 = Lower)", [1, 2, 3])
    p_sex = st.selectbox("Sex", ["male", "female"])
    p_age = st.number_input("Age", 0, 100, value=30)

with col2:
    p_sibsp = st.number_input("Number of Siblings/Spouses", 0, 10, value=0)
    p_parch = st.number_input("Number of Parents/Children", 0, 10, value=0)
    p_fare = st.number_input("Fare", 0.0, 1000.0, value=30.0)

p_embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])


# Encoded
sex_encoded = le_sex.transform([p_sex])[0]
embarked_encoded = le_embarked.transform([p_embarked])[0]

#Predict
if st.button("Predict Survival"):
    input_data = np.array([[p_class, sex_encoded, p_age, p_sibsp, p_parch, p_fare, embarked_encoded]])
    predicted_result = model.predict(input_data)

    if predicted_result[0] == 1:
        st.success("The passenger is likely to survive.")
    else:
        st.error("The passenger is likely not to survive.")



# Visualizations
# ---- DATA INSIGHTS ----
st.markdown("---")
st.header("📊 Data Insights from the Titanic Dataset")

# Load dataset
data = pd.read_csv("Titanic-Dataset.csv")

# Interactive Age vs Survival
st.subheader("👶 Age vs Survival (Interactive)")

age_fig = px.histogram(data, x="Age", color="Survived",
                      nbins=30, barmode="stack",
                      title="Age Distribution by Survival",
                      labels={"Age": "Age", "count": "Number of Passengers", "Survived": "Survival Status"},
                      color_discrete_map={0: "#EF4444", 1: "#10B981"})
st.plotly_chart(age_fig, use_container_width=True)


# Interactive Sex vs Survival
st.subheader("👫 Sex vs Survival (Interactive)")

sex_fig = px.histogram(data, x="Sex", color="Survived",
                      title="Number of Passengers by Sex and Survival",
                      labels={"count": "Number of Passengers", "Sex": "Sex", "Survived": "Survival Status"},
                      color_discrete_map={0: "#EF4444", 1: "#10B981"})
st.plotly_chart(sex_fig, use_container_width=True)


# Interactive Fare vs Survival
st.subheader("💵 Fare vs Survival (Interactive)")

fare_fig = px.box(data, x="Survived", y="Fare",
                  title="Fare vs Survival",
                  labels={"Fare": "Fare ($USD)", "Survived": "Survival Status"},
                  color="Survived",
                  color_discrete_map={0: "#EF4444", 1: "#10B981"})
st.plotly_chart(fare_fig, use_container_width=True)

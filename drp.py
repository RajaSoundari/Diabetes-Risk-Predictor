import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(layout="wide")

st.markdown(f""" <style>.stApp {{
                        background:url("https://plus.unsplash.com/premium_photo-1671482215345-3c7001c4e31f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80.jpg");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: purple;'>Diabetes Detective: Predicting Your Diabetes Risk</h1>",
            unsafe_allow_html=True)

selected = option_menu(None, ["About","Predict"],
                       icons=["house-fill","heart-pulse-fill"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "35px", "text-align": "centre", "margin": "-2px", "--hover-color": "#0c457d"},
                               "icon": {"font-size": "35px"},
                               "container" : {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "#6495ED"}})


df=pd.read_csv("C:/Users/USER/Documents/ds/PROJECT/Untitled Folder/diabetes_prediction_dataset.csv")

from sklearn.preprocessing import OrdinalEncoder
enc=OrdinalEncoder()

df["smoking_history"]=enc.fit_transform(df[["smoking_history"]])
df["gender"]=enc.fit_transform(df[["gender"]])

x= df.drop("diabetes",axis=1)
y=df["diabetes"]

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier().fit(x,y)

if selected == "About":
    
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Welcome to the Diabetes Risk Predictor!")
        st.write("   Our tool helps you understand your risk of developing diabetes.")
        st.write("Simply provide the information asked in the next page about yourself, and we'll provide you with an assessment.")
        st.write("Take the first step towards a healthier future. Start your risk assessment now!")
        with st.container():
            st.image("https://cdnl.iconscout.com/lottie/premium/thumb/health-checkup-5663463-4718692.gif")
    with right_column:
        st.subheader("About Diabetes:")
        
        st.write("Diabetes is a prevalent and serious health condition that affects millions of people worldwide. It's important to assess your risk factors and make informed choices for a healthier life.")
        st.write("According to the Centers for Disease Control and Prevention’s National Diabetes Statistics Report, an estimated 37.3 million people in the United States, or 11.3% of the population, have diabetes. About 1 in 4 adults with diabetes don’t know they have the disease. An estimated 96 million American adults have prediabetes, which means their blood glucose levels are higher than normal but not high enough to be diagnosed as diabetes.")
        st.write("To learn more about diabetes, please visit the Diabetes Association Of Inida Official Page")
        st.write("https://idf.org/our-network/regions-and-members/south-east-asia/members/india/diabetic-association-of-india/")

    

    


if selected == "Predict":
    Gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    Age = st.number_input("Enter your age:")
    Hypertension = st.selectbox("Could you please let us know if you have been diagnosed with hypertension?:", ["Yes", "No"])
    Heart_Disease = st.selectbox("Do you have a history of heart disease?:", ["Yes", "No"])
    Smoking_History = st.selectbox("Kindly choose your smoking background:", [
        'I have never smoked',
        "I don't have information about my smoking history",
        'I currently smoke',
        'I used to smoke, but I quit',
        'I have tried smoking in the past, but I am not currently a smoker',
        "I'm not smoking right now"
    ])
    Bmi = st.number_input("Enter your BMI:")
    HbA1c_level = st.number_input("Enter your HbA1c level:")
    blood_glucose_level = st.number_input("Enter your blood glucose level:")

    data = {
        "gender": [Gender],
        "age": [Age],
        "hypertension": [Hypertension],
        "heart_disease": [Heart_Disease],
        "smoking_history": [Smoking_History],
        "bmi": [Bmi],
        "HbA1c_level": [HbA1c_level],
        "blood_glucose_level": [blood_glucose_level]

    }
    if st.button("Confirm"):
        df1 = pd.DataFrame(data)

        df1["gender"]  = df1["gender"].map({'Male':1,"Female":2,"Other":2})
        df1["smoking_history"]  = df["smoking_history"].map({'I have never smoked':4,"I don't have information about my smoking history":0,'I currently smoke':1,'I used to smoke, but I quit':3,'I have tried smoking in the past, but I am not currently a smoker':2,"I'm not smoking right now":5})
        df1["hypertension"]  = df1["hypertension"].map({'Yes':1,"No":0})
        df1["heart_disease"]  = df1["heart_disease"].map({'Yes':1,"No":0})

        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier().fit(x,y)
        y_pred = model.predict(df1)

        if y_pred == 0:
            st.success("Great news! Based on the information you provided, there is no indication that you have a high risk of diabetes.")
            st.success("Maintaining a healthy lifestyle, such as regular exercise and a balanced diet, can help you continue on your path to good health.")
        else:
            st.success("Caution! Based on the information you provided, there is a possibility that you may have an elevated risk of diabetes.")
            st.success("It's important to consult with a healthcare professional for further evaluation and guidance on managing your health.")







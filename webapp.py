import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

st.set_page_config(page_title='Student Pass/Fail Forecaster', page_icon="https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books_23-2149342941.jpg?w=2000", layout="wide", initial_sidebar_state="auto", menu_items=None)

def predict(sex = 'F',
            age = 18,
            Medu = '4',
            reason = 'home',
            traveltime = 2,
            studytime = 2,
            freetime = 4,
            higher = 'yes',
            failures = 0,
            internet = 'yes'):

    new_data = {
    'sex': sex,
    'age': age,
    'Medu': Medu,
    'reason': reason,
    'traveltime': traveltime,
    'studytime': studytime,
    'freetime': freetime,
    'higher': higher,
    'failures': failures,
    'internet': internet
}

    X_pred = pd.DataFrame(new_data, index=[0])

    model = joblib.load("pipeline4.joblib")
    prediction = model.predict(X_pred)

    if prediction[0] == 1:
        result = "Pass"
    else:
        result = "Fail"

    return result

# Add a title and intro text
st.title('Student Pass/Fail Forecaster')
st.text('This is a web app to which predicts whether a high-school student will pass or fail depending on a set of variables')


# Create a section for the user inputs
st.header('Create the student profile')

col1, col2 = st.columns(2,gap="medium")

with col1:

    sex = st.selectbox('SEX:', ('M', 'F'), index=0)
    age = st.number_input(label='AGE', value=18,max_value=21, min_value=15)
    higher = st.selectbox('Interested in higher education?', ('yes', 'no'), index=0)
    reason = st.selectbox('Reason for choosing school:', ('reputation','course','home', 'other'), index=0)
    internet = st.selectbox('Internet connection at home', ('yes', 'no'), index=0)

with col2:
    Medu = st.select_slider('Mothers education (1 is lowest level of education)', (1,2,3,4),value=1)
    studytime = st.select_slider('Weekly study time (1: <2 hrs, 2: 2-5 hrs, 3: 5-10 hrs, 4: >10 hrs):', (1, 2, 3, 4),value=1)
    freetime = st.select_slider('Weekly free time (1: very low, 5: very high):', (1, 2, 3, 4, 5),value=1)
    traveltime = st.select_slider('Travel time to school (1: <15mins, 2: 15-30mins, 3: 30-60mins, 4: >60mins):', (1, 2, 3, 4),value=1)
    failures = st.select_slider('Number of previous failures', (0,1,2,3),value=0)

# Create a section for the dataframe statistics
st.header('Summary of student profile')

data = pd.DataFrame({'Sex': [sex], 'Age': [age], 'Mother Education': [Medu], 'Reason for choosing school': [reason], 'Travel time': [traveltime], 'Study time': [studytime], 'Free time': [freetime], 'Plans for higher education': [higher], 'Number of failures': [failures], 'Access to internet': [internet]})

st.write(data)

# Create a section for prediction
st.header('Prediction of pass or fail for student')

col3, col4, col5 = st.columns(3,gap="large")

with col4:
    submitted = st.button('SUBMIT')
    if submitted:
        answer = predict(sex, age, Medu, reason, traveltime, studytime, freetime, higher, failures, internet)
        if answer == "Pass":
            st.title(f'Prediction: :green[{answer}]')
        else:
            st.title(f'Prediction: :red[{answer}]')

import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.write("Student Forecaster")

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

    model = joblib.load("pipeline3.joblib")
    prediction = model.predict(X_pred)

    if prediction[0] == 1:
        result = "Pass"
    else:
        result = "Fail"

    return result


sex = st.selectbox('SEX:', ('M', 'F'))
age = st.number_input(label='AGE', value=18)
Medu = st.select_slider('Mothers education (1 is lowest level of education)', (1,2,3,4))
reason = st.selectbox('Reason for choosing school:', ('reputation','course','home', 'other'))
traveltime = st.select_slider('Travel time to school (1: under 15mins, 2: 15-30mins, 3: 30-60mins, 4: More than 60mins):', (1, 2, 3, 4))
studytime = st.select_slider('Weekly study time (1: less than 2 hours, 2: 2-5 hours, 3: 5-10 hours, 4: Greater than 10 hours):', (1, 2, 3, 4))
freetime = st.select_slider('Weekly free time (1: very low, 5: very high):', (1, 2, 3, 4, 5))
higher = st.selectbox('Interested in higher education?', ('yes', 'no'))
failures = st.select_slider('Number of previous failures', (0,1,2,3))
internet = st.selectbox('Internet connection at home', ('yes', 'no'))

submitted = st.button('SUBMIT')
if submitted:
    st.write(predict(sex, age, Medu, reason, traveltime, studytime, freetime, higher, failures, internet))

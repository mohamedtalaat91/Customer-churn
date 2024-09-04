import streamlit as st
import pandas as pd
import joblib
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv(r"Deployment/source/cleaned_data.csv")

st.markdown("<h1 style='text-align: center;'>Customer Churn Prediction Page</h1>", unsafe_allow_html=True)
st.markdown("<h5> ABOUT CHURN PREDICTION</h5>", unsafe_allow_html=True)
st.write("This a page dedicated to predict customer churn. ")
st.write("using a Random Forest Classifier model traind and tested over our dataset. ")
st.write("The model is making an accuracy of 97.7%  over the test set. ")
st.write("Enter the required data accurately for providing an accurate prediction. ")

st.markdown("<h5> INPUT DATA FOR CHURN PREDICTION</h5>", unsafe_allow_html=True)
col1, col2= st.columns([1,1])
with col1:
    tenure = st.number_input('Enter your tenure in the organization',min_value=0, value=1)
    warehousetohome = st.number_input('Enter your warehousetohome',min_value=0, value=1)
    hourspendonapp = st.number_input('Enter your Hour Spent An App',min_value=0, value=1)
    numberofdeviceregistered = st.number_input('Enter your number of device registered',min_value=1, value=1)
    satisfactionscore = st.number_input('Enter your Satisfaction Score',min_value=0, value=1,max_value=5)
    numberofaddress = st.number_input('Enter your number of address',min_value=0, value=1)
    OrderAmountHike = st.number_input('Enter your Order Amount Hike',min_value=0, value=1)
    couponused = st.number_input('Enter your coupon used',min_value=0, value=1)
    daysincelastorder = st.number_input('Enter your days since last order',min_value=0, value=1)







with col2:
    preferredlogindevice = st.selectbox('select your preferred login device',['Phone', 'Mobile Phone','Computer'])
    citytire = st.selectbox('Select your city tire',[1,2,3])
    preferredpaymentmode = st.selectbox('select your preferred payment mode',['Debit Card','Credit Card','E wallet', 'UPI', 'COD', 'CC', 'Cash on Delivery'])
    gender = st.selectbox('select your gender',['Male','Female'])
    preferedordercat = st.selectbox('select your prefered order category',['Laptop & Accessory', 'Mobile Phone', 'Fashion', 'Mobile', 'Grocery','Others'])
    maritalstatus = st.selectbox('select your marital status',['Single', 'Married', 'Divorced'])
    complain = 0 if st.radio("Have you made a complain", ("Yes", "No")) == "NO" else 1
    cashbackamount = st.number_input('Enter your cashback amount',min_value=1, value=1)
    ordercount = st.number_input('Enter your order count',min_value=1, value=1)


input_data = pd.DataFrame({
    'tenure': [tenure],
    'preferredlogindevice': [preferredlogindevice],
    'citytier': [citytire],
    'warehousetohome': [warehousetohome],
    'preferredpaymentmode': [preferredpaymentmode],
    'gender': [gender],
    'hourspendonapp': [hourspendonapp],
    'numberofdeviceregistered': [numberofdeviceregistered],
    'preferedordercat': [preferedordercat],
    'satisfactionscore': [satisfactionscore],
    'maritalstatus': [maritalstatus],
    'numberofaddress': [numberofaddress],
    'complain': [complain],
    'orderamounthikefromlastyear': [OrderAmountHike],
    'couponused': [couponused],
    'ordercount' : [ordercount],
    'daysincelastorder' : [daysincelastorder],
    'cashbackamount' : [cashbackamount]
})

st.markdown("<h5> CLICK TO PREDICT</h5>", unsafe_allow_html=True)
data.drop(['customerid' , 'churn'] , inplace = True ,axis = 1)
import pickle

# Load the saved pipeline
with open('Deployment/source/churn_model_pipeline.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)


# Use the pipeline to make predictions

prediction = model_pipeline.predict(input_data)

if st.button('Predict'):
    if prediction[0] == 0:
        st.success('Your customer will Not churn ')
    elif prediction[0] == 1:
        st.error('Your customer will  churn ')

# Now you can use `model_pipeline` to make predictions





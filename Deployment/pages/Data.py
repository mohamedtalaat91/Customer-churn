import pandas as pd 
import streamlit as st 
from zipfile import ZipFile




zip_file_path = "Deployment/source/churn.csv"
data = pd.read_csv(zip_file_path)

st.markdown('''<center> <h1> Customer Churn Data Discription </h1> </center>''',unsafe_allow_html=True)
disc = pd.read_csv("Deployment/source/description.csv" ,index_col='column')
st.write(disc)
st.markdown('''<center> <h1> Customer Churn Data </h1> </center>''',unsafe_allow_html=True)
st.markdown('<a href ="https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/data"> <center> <h2> Link </h2> </center> ', unsafe_allow_html=True)
st.write(data)


import streamlit as st

st.markdown('''<center> <h1> About </center>''', unsafe_allow_html=True)

st.markdown(
    """ <center> <h5>
    This web app is created using Streamlit.
               </center>""",unsafe_allow_html=True)

st.markdown(
    """<h4> <br> <br>
    Analysis about Customer Churn.
               </h4""",unsafe_allow_html=True)

st.markdown("""<h6>
    about data :
               </h6>""",unsafe_allow_html=True)

st.write("This Data set is about Customer Churn. ")     
st.write("The data set belongs to a leading online E-Commerce company. An online retail (E commerce) company wants to know the customers who are going to churn, so accordingly they can approach customer to offer some promos.") 
st.write( "The data was obtained from  https://www.kaggle.com/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction" )           
st.markdown("""<h6> <br>
    About  The Analysis Flow :
               </h6>""",unsafe_allow_html=True)  
st.write(" 1- Load the data ")
st.write( "2- explore the data") 
st.write(" 3- clean the data ")
st.write(" 4- perform EDA and gain insights")
st.write(" 5- Tuning Machine Learning models for Prediction")    
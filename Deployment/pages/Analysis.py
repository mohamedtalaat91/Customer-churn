import MEDA as md
import pandas as pd
import streamlit as st
import joblib

data = pd.read_csv(r"E:\Epsilon AI\final_project\Deployment\source\churn.csv")
data = md.clean_data(data)
data = md.treat_outliers(data)


st.markdown("<h1 style='text-align: center;'>Customer Churn Analysis Page</h1>", unsafe_allow_html=True)

tap1 , tap2 = st.tabs(["OVERALL ANALYSIS","CHURNED CUSTOMERS ANALYSIS"])

with tap1 :
    st.markdown("<h3>1. OVERALL ANALYSIS</h3>", unsafe_allow_html=True)
    st.markdown("<h5>1.1.  ABOUT ANALYSIS</h5>", unsafe_allow_html=True)
    st.write("This analysis is about all of our customers . ")
    st.write ("analyzing all customers to know the distributions of our customers over each category. ")
    st.write("The data is cleaned and treated outliers to remove the outliers and outliers will affect the analysis.")


    st.markdown("<h5>1.2.  Numerical Values Distributions </h5>", unsafe_allow_html=True)

    st.plotly_chart(md.plot_numeric_distributions(data))
    st.markdown("<h5> Insights : </h5>", unsafe_allow_html=True)
    st.write("Most of the customers have Tenure of 1.")
    st.write("Most of the customers have Distance from home as 9 And 14 km.")
    st.write("Most of the customers have spent around 3 Hours on the App. ")
    st.write("Most of the customers have 4 Registered Devices. ")
    st.write("Most of the customers have Satisfiction score of 4. ")
    st.write("Most of the customers have  2 or 3 number of addresses. ")
    st.write("Most of the customers have  between 12 and 15 orders Hike from last year. ")
    st.write("Most of the customers have Used only 1 coupon. ")
    st.write("Most of the customers have order counts of 1 or 2 ")
    st.write("Most of the customers is making orders with 1 to 3 days in between. ")
    st.write("Most of the customers have a cashback amount between 120 and 160. ")



# _________________________________________________________________

    st.markdown("<h5>1.3.  Categorical Values Distributions </h5>", unsafe_allow_html=True)

    st.plotly_chart(md.plot_categorical_distributions(data))

    st.markdown("<h5> Insights : </h5>", unsafe_allow_html=True)

    st.write("Most of the customers are Not Churned customers. ")
    st.write("Most of the customers are preferring using Mobile Phone. ")
    st.write("Most of the customers in the city tier 1. ")
    st.write("Most of the customers are using Depit card or Cash on Delivery. ")
    st.write("Most of the customers are Male. ")
    st.write("Most of the customers prefers ordering Laptop & accessories. ")
    st.write("Most of the customers are Married. ")
    st.write("Most of the customers wasn't complained. ")

with tap2:
    st.markdown("<h3>2. CHURNED CUSTOMERS ANALYSIS</h3>", unsafe_allow_html=True)
    st.markdown("<h5>2.1.  ABOUT CHURNED CUSTOMERS</h5>", unsafe_allow_html=True)

    st.write("This analysis is about all of our Churned customers . ")
    st.write("The churned customers are the ones who left the company. ")
    st.write("analyzing the churned customers to know the distributions of our churned customers over each category. ")
    st.write("The provided plots will make a clear picture of the percaentage of churned customers from all our customers in each category. ")


    
    st.markdown("<h5>2.1.  Interactive Plot to analyze Churned Customers</h5>", unsafe_allow_html=True)
    st.markdown("choose the column to make a plot of the distribution of churned customers and the percentage of churned customers in each category. ")
       
    column = st.selectbox("Select Column",data.columns)
    st.plotly_chart(md.generate_churn_analysis_plot(data,column ))
    # _____________________________________________

    st.markdown("<h5>2.2.  Subplots to analyze Churned Customers</h5>", unsafe_allow_html=True)
    st.write("The subplots will make a clear picture of the percaentage of churned customers from all our customers in each category. ")

    st.plotly_chart(md.generate_churn_analysis_subplots(data))
    st.markdown("<h5> Insights : </h5>", unsafe_allow_html=True)

    st.write("the Avarage persentage of churned customers from all our customers is 20.25%. ")
    st.write("the persentage of churned customers is increasing in the customers that prefer using Phone as login device as percentage is 22.4% . ")
    st.write("the persentage of churned customers is increasing in the customers in city tier 3 as percentage is 21.3 %. ")
    st.write("the persentage of churned customers is increasing in the customers that use COD payment method as percentage is 28.7%. ")

    st.write("the persentage of churned customers is increasing in the customers that are Male as percentage is 17.7 %. ")
    st.write("the persentage of churned customers is increasing in the customers that prefer ordering Mopile and Mopile Phones as percentage is around 27 % for each. ")
    st.write("the persentage of churned customers is increasing in the customers that are Single as percentage is 26.7. ")
    st.write("the persentage of churned customers is increasing in the customers that was made a complain as percentage is 31.6 % . ")





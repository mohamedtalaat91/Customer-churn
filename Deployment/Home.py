import numpy as np 
import pandas as pd
import streamlit as st


st.markdown("<h1 style='text-align: center;'>Customer Churn</h1>", unsafe_allow_html=True)
st.markdown('''
<center> <h5>
            This project is for Analyizing And Predicting Customer Churn .
            </center> </h5>''',unsafe_allow_html=True)


col1, col2, col3 = st.columns([1,3,1])
# Display the GIF in the middle column to center it
with col2:
    st.image("https://media.licdn.com/dms/image/v2/C4E12AQH1tX6PrSgzbg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1647940360448?e=1730937600&v=beta&t=20BEFE90UjtkM64hf6EGn569P7WsZ8YTNixLJEEn8b4", width=500)
st.markdown('''
<center> <h10>
            Done by : Mohamed Talaat <br>
            Supervised by : Epsilon AI <br>
            
            ''',unsafe_allow_html=True)
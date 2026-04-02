import streamlit as st
import numpy as np
import pandas as pd

st.title('Weather Prediction App')

st.sidebar.header('User Input')
temp = st.sidebar.slider('Temperature (F)', min_value=32, max_value=100, value=70)
humidity = st.sidebar.slider('Humidity (%)', min_value=0, max_value=100, value=50)
precipitation = st.sidebar.slider('Precipitation (inches)', min_value=0.0, max_value=5.0, value=1.0)

st.subheader('Your Input Values')
st.write(f'Temperature: {temp} F')
st.write(f'Humidity: {humidity}%')
st.write(f'Precipitation: {precipitation} inches')

st.subheader('Prediction')
prediction = np.random.rand() * 100
st.write(f'Predicted Temperature: {prediction:.2f} F')

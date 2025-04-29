import streamlit as st
import pandas as pd


st.title("BMI Calculator")

height = st.slider("Enter your height (in cm)", 100, 250, 175)
weight = st.slider("Enter your weight (in kg)", 30, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is: {bmi:.2f}")
st.write("BMI Categories:")
st.write("Underweight: Less than 18.5")
st.write("Normal weight: 18.5 and 24.9")
st.write("Overweight: 25 and 29.9")
st.write("Obesity: 30 or greater")
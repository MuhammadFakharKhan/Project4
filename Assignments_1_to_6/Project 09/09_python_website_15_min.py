import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="My Streamlit Dashboard", page_icon="📊")

def main():
    
    
    st.title("Welcome to My Interactive Dashboard! 🚀")
    st.write("This is a simple web app built with Streamlit to showcase data and user interaction in just 15 minutes!")
    
    
    user_name = st.text_input("What's your name?", "Type here...")
    if user_name and user_name != "Type here...":
        st.write(f"Hello, {user_name}! Enjoy exploring the dashboard!")
    
    
    data_size = st.slider("Select number of data points to display", min_value=10, max_value=100, value=50)
    
    
    np.random.seed(42)
    data = pd.DataFrame({
        "X": range(data_size),
        "Y": np.random.randn(data_size) * 10,
        "Category": np.random.choice(["A", "B", "C"], data_size)
    })
    
    
    st.header("Sample Dataset")
    st.dataframe(data, use_container_width=True)
    
    
    st.header("Data Visualization")
    fig = px.scatter(data, x="X", y="Y", color="Category", title="Random Data Scatter Plot",
                     labels={"X": "Index", "Y": "Value"},
                     template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    
    st.sidebar.header("Customize Your Dashboard")
    show_raw_data = st.sidebar.checkbox("Show raw data details", value=False)
    if show_raw_data:
        st.header("Raw Data Statistics")
        st.write(data.describe())
    
    
    if st.button("Generate New Data"):
        st.rerun()  

if __name__ == "__main__":
    main()

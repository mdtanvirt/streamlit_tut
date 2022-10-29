import streamlit as st
import pandas as pd
from matplotlib import  pyplot as plt
from plotly import graph_objs as go

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    header {visibility: hidden}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

data = pd.read_csv("data//dalary_data.csv")

st.title("Salary predictor")
nav = st.sidebar.radio("Navigation", ["Home", "Prediction", "Conribute"])

if nav == "Home":
    st.write("Well come to salary prediction calculator")
    if st.checkbox("Show raw data"):
        st.table(data)

    grapg = st.selectbox("What kind of Graph?", ["Non-Interactive", "Interactive"])

    val = st.slider("Filter data using year of experience", 0,20)
    data = data.loc[data["YearsExperience"] >= val]
    
    if grapg == "Non-Interactive":
        plt.figure(figsize=(10, 5))
        plt.scatter(data["YearsExperience"], data["Salary"])
        plt.ylim(0)
        plt.xlabel("Year of Enperience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()

    if grapg == "Interactive":
        layout = go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range=[0, 210000])
        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode="markers"), layout=layout)
        st.plotly_chart(fig)

if nav == "Prediction":
    st.write("Prediction")

if nav == "Conribute":
    st.write("Conribute")
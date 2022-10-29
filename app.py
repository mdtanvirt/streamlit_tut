import streamlit as st
import pandas as pd
from matplotlib import  pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

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

x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x, np.array(data["Salary"]))

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
    st.header("Know your salary")
    val = st.number_input("Enter your year of experience", 0.00, 20.00, step=0.25)
    val = np.array(val).reshape(1, -1)
    predict = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(predict)}")

if nav == "Conribute":
    st.header("contribute our database")
    exp = st.number_input("Your year of experience", 0.00, 20.00)
    slr = st.number_input("Your salary", 0.00, 200000.00, step=1000.00)
    if st.button("Submit"):
        to_add = {"YearsExperience":[exp], "Salary":[slr]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//dalary_data.csv", mode='a', header=False, index=False)
        st.success("Submitted")
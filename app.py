from unicodedata import name
import streamlit as st

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    header {visibility: hidden}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Wedgets")
if st.button("Subscribe"):
    st.write("Like this video too")

name = st.text_input("Full Name")
st.write(name)

address = st.text_area("Enter your Address")
st.write(address)

st.date_input("Enter a date")

st.time_input("Enter time")

if st.checkbox("You have to accept the T&C", value=False):
    st.write("Thank you")

v1 = st.radio("Color", ["r", "g", "b"], index=0)
v2 = st.selectbox("Color", ["r", "g", "b"], index=1)

st.write(v1, v2)

v3 = st.multiselect("Color", ["r", "g", "b"])
st.write(v3)

st.slider('age', min_value=18, max_value=60, value=30, step=2)

st.number_input("Number", min_value=18.0, max_value=60.0, value=30.0, step=2.0)

st.file_uploader("Upload a file")

st.sidebar.title("This is sidebar")
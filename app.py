from unicodedata import name
import streamlit as st

st.title("Wedgets")
if st.button("Subscribe"):
    st.write("Like this video too")

name = st.text_input("Full Name")
st.write(name)

address = st.text_area("Enter your Address")
st.write(address)

st.date_input("Enter a date")

st.time_input("Enter time")
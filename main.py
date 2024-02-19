import streamlit as st

st.write("#welcome")

num1=st.text_input("enter a number")
num2=st.text_input("enter next number")

if st.button("Add"):
    st.write(f"#the total is {int(num1)+int(num2)}")
    st.balloons()
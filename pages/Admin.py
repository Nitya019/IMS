import streamlit as st

import pandas as pd


# temporary credentials
user_name = "admin"
pass_word= "password123"

# Session state 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
    
def login():
    st.title("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type = "password")
    if st.button("Login"):
        if username == user_name and password == pass_word:
            st.session_state.logged_in = True
            st.balloons()
        else:
            st.error("Invalid credentials")
            
            


if st.session_state.logged_in:
    pass
else:
    login()

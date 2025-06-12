import streamlit as st


# temporary credentials
user_name = "admin"
pass_word= "password123"

# Session state 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
    
def login():
    st.title("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password")
    if st.button("Login"):
        if username == USERN
#--------------Importing modules--------------------------#
import streamlit as st
import pandas as pd
import os

#-------------load the database---------------------------#
df = pd.read_csv("data.csv", delimiter="\t", encoding ="utf-16")



# temporary credentials
user_name = "admin"
pass_word= "password123"

# Session state 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


#-------------Function for login--------------------------#
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
            

#----------------------ADD ITEM---------------------------#
st.title("ADMIN DASHBOARD")
tab1, tab2, tab3 = st.tabs(["ADD", "UPDATE", "DELETE"])

with tab1:
    st.subheader("ADD NEW ITEM")
    uid = st.text_input("UID")
    Category = st.text_input("Item Name")
    Subcategory = st.text_input("Subcategory")
    Metal = st.selectbox("Metal", ("Gold","Silver"))
    Purity = st.selectbox("Purity", ("18K","22K"))
    Weight = st.number_input("Weight")
    Image = st.text_input("Image path (e.g. images/set1/img1.png)")

if st.button("ADD"):
    new_data = pd.DataFrame([[uid, Category, Subcategory,Metal, Purity, Weight, Image]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index= True)
    df.to_csv(df, index =False)
    st.success(f"{Category} added successfully! ")


#----------------------DELETE ITEM---------------------------#



if st.session_state.logged_in:
    pass
else:
    login()

#--------------Importing modules--------------------------#
import streamlit as st
import pandas as pd
import os

#-------------load the database---------------------------#
df = pd.read_csv("data.csv", delimiter= '\t', encoding='utf-8')

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

            
if st.session_state.logged_in:

#----------------------ADD ITEM---------------------------#
    st.title("ADMIN DASHBOARD")
    tab1, tab2, tab3 = st.tabs(["ADD", "UPDATE", "DELETE"])

    with tab1:
        st.subheader("ADD NEW ITEM")
        uid = st.text_input("UID")
        Category = st.text_input("Item Name")
        Metal = st.selectbox("Metal", ("Gold","Silver"))
        Purity = st.selectbox("Purity", ("18K","22K"))
        Weight = st.number_input("Weight")
        Image = st.text_input("Image path (e.g. images/set1/img1.png)")

    if st.button("ADD"):
        new_data = pd.DataFrame([{
            "uid": uid,
            "Category": Category,
            "Metal": Metal,
            "Purity": Purity,
            "Weight": Weight,
            "Image": Image
        }])
    
        df = pd.concat([df, new_data], ignore_index= True)
        df.to_csv("data.csv", index =False)
        st.success(f"{Category} added successfully! ")


    #----------------------DELETE ITEM---------------------------#
    with tab3:
        st.subheader("DELETE AN ITEM")
        if df.empty:
            st.warning("No items to delete")
        else:
            delete_item = st.selectbox("Select item to delete", df["uid"])
            if st.button("Delete"):
                df = df[df["uid"] != delete_item]
                df.to_csv("data.csv",index = False)
                st.success(f"{delete_item} deleted successfully!")


    # --- Display Table ---
    st.divider()
    st.subheader("📋 Current Inventory")
    st.dataframe(df)

if st.session_state.logged_in:
    pass
else:
    login()

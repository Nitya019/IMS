#-----------importing modules-------------------------------#
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


with open('/config.yaml') as file:
    config = yaml.load(file, Loader= SafeLoader)

#------------cleaning the data a bit-----------------------#
df = pd.read_csv("data.csv", delimiter="\t", encoding ="utf-16")
df["Category"] = df["Category"].str.strip().str.title()

#------------extracting data--------------------------------#

earring_df = df[df["Category"] == "Earring"]
set_df = df[df["Category"] == "Set"]
brace_df = df[df["Category"]== "Bracelet"]
ms_df = df[df["Category"] == "Mangalsutra"]


#-------------functions for each product----------------------#
def ear_page():
    st.title("Earring Collection")
    for _, row in earring_df.iterrows():
        st.image(row['Image'], width=200)
        st.write(f"Weight: {row['Weight']}")
        st.write(f"Purity: {row['Purity']}")
        st.write(f"ID: {row['UID']}")
        st.markdown("---")


def set_page():
        st.title("Set Collection")
        for _, row in set_df.iterrows():
            st.image(row['Image'], width=200)
            st.write(f"Weight: {row['Weight']}")
            st.write(f"Purity: {row['Purity']}")
            st.write(f"ID: {row['UID']}")
            st.markdown("---")


def br_page():
        st.title("Bracelet Collection")
        for _, row in brace_df.iterrows():
            st.image(row['Image'], width=200)
            st.write(f"Weight: {row['Weight']}")
            st.write(f"Purity: {row['Purity']}")
            st.write(f"ID: {row['UID']}")
            st.markdown("---")


def ms_page():
    st.title("Mangalsutra Collection")
    for _, row in ms_df.iterrows():
        st.image(row['Image'], width=200)
        st.write(f"Weight: {row['Weight']}")
        st.write(f"Purity: {row['Purity']}")
        st.write(f"ID: {row['UID']}")
        st.markdown("---")




#----------------adding the sidebar-------------------------#
st.sidebar.title("Inventory")

opt = st.sidebar.selectbox(
    "Choose a product", ["Earrings", "Sets", "Bracelets", "Mangalsutra"]
)

if opt == "Earrings":
    ear_page()
    
if opt == "Sets":
    set_page()

if opt == "Bracelets":
    br_page()

if opt == "Mangalsutra":
    ms_page()
    

opt2 = st.sidebar.selectbox("Choose an option", ["Add", "Delete", "Update"])


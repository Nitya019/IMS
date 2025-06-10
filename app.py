import streamlit as st

import pandas as pd


df = pd.read_csv("data.csv", delimiter="\t", encoding ="utf-16")
df["Category"] = df["Category"].str.strip().str.title()

earring_df = df[df["Category"] == "Earring"]
set_df = df[df["Category"] == "Set"]
brace_df = df[df["Category"]== "Bracelet"]

def ear_page():
    st.title("Earring Collection")
    for _, row in earring_df.iterrows():
        st.image(row['ImagePath'], width=400)
        st.write(f"Weight: {row['Weight']}")
        st.write(f"Purity: {row['Purity']}")
        st.write(f"ID: {row['UID']}")
        st.markdown("---")


def set_page():
        st.title("Set Collection")
        for _, row in set_df.iterrows():
            st.image(row['ImagePath'], width=400)
            st.write(f"Weight: {row['Weight']}")
            st.write(f"Purity: {row['Purity']}")
            st.write(f"ID: {row['UID']}")
            st.markdown("---")


def br_page():
        st.title("Bracelet Collection")
        for _, row in brace_df.iterrows():
            st.image(row['ImagePath'], width=200)
            st.write(f"Weight: {row['Weight']}")
            st.write(f"Purity: {row['Purity']}")
            st.write(f"ID: {row['UID']}")
            st.markdown("---")








st.sidebar.title("Inventory")

opt = st.sidebar.selectbox(
    "Choose a product", ["Earrings", "Sets", "Bracelets"]
)

if opt == "Earrings":
    ear_page()
    
if opt == "Sets":
    set_page()

if opt == "Bracelets":
    br_page()

'''
import streamlit as st
import pandas as pd

def show_earrings():
    st.title("Earring Collection")


df = pd.read_csv("data.csv", delimiter="\t", encoding ="utf-16")
df["Category"] = df["Category"].str.strip().str.title()

# Filter only set
earring_df = df[df["Category"] == "Set"]

for _, row in earring_df.iterrows():
    st.image(row['ImagePath'], width=200)
    st.write(f"Weight: {row['Weight']}")
    st.write(f"Purity: {row['Purity']}")
    st.write(f"ID: {row['UID']}")
    st.markdown("---")
    
    '''
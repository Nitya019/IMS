
"""
import streamlit as st
import pandas as pd

def show_sets():
    st.title("Set Collection")


df = pd.read_csv("data.csv", delimiter="\t", encoding ="utf-16")
df["Category"] = df["Category"].str.strip().str.title()

# Filter only set
set_df = df[df["Category"] == "Set"]

for _, row in set_df.iterrows():
    st.image(row['ImagePath'], width=200)
    st.write(f"Weight: {row['Weight']}")
    st.write(f"Purity: {row['Purity']}")
    st.write(f"ID: {row['UID']}")
    st.markdown("---")
    
    """
import streamlit as st
import pandas as pd

def show_earrings():
    st.title("Earring Collection")
# Load your CSV and clean it up a bit...
df = pd.read_csv("data.csv", delimiter="\t", encoding ="utf-16")
df["Category"] = df["Category"].str.strip().str.title()

"""
for row in df:
    if (df["Category"] == "Earring").any():
        st.image(f"images/{row['Image']}", width=200)
        st.write(f"Weight: {row['Weight']}")
        st.write(f"Purity: {row['Purity']}")
        st.write(f"ID: {row['UID']}")
        st.markdown("---")
"""


for _, row in df.iterrows():
    st.image(f"images/{row['ImagePath']}", width=200)
    st.write(f"Weight: {row['Weight']}")
    st.write(f"Purity: {row['Purity']}")
    st.write(f"ID: {row['UID']}")
    st.markdown("---")
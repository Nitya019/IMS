import streamlit as st
import pandas as pd


def show_sets():
    st.title("Set Collection")


df = pd.read_csv("data.csv" ,encoding='utf-16')  # Ensure this file exists and has correct columns

for row in df:
    if (row == "Category" and  df[df["Category"] == "Earring"]):
        st.image(f"images/{row['Image']}", width=200)
        st.write(f"Weight: {row['Weight']}")
        st.write(f"Purity: {row['Purity']}")
        st.write(f"ID: {row['UID']}")
        st.markdown("---")
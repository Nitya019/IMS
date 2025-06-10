import streamlit as st
import pandas as pd

def show_sets():
    st.title("Set Collection")


df = pd.read_csv("data.csv", delimiter="\t", encoding ="utf-16")
df["Category"] = df["Category"].str.strip().str.title()
df['ImagePath'] = df['ImagePath'].str.replace(r'^images/', '', regex=True)


for _, row in df.iterrows():
    st.image(row['ImagePath'], width=200)
    st.write(f"Weight: {row['Weight']}")
    st.write(f"Purity: {row['Purity']}")
    st.write(f"ID: {row['UID']}")
    st.markdown("---")
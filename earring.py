import streamlit as st 
import pandas as pd 
import os

st.markdown("""
    <style>
    .big-font {
        font-size:75px !important;
        color:white;
        text-align: center;
        font-family: 'Roboto', Monospace; 
    }
    </style>
    <div class="big-font">VN JEWELLERS<div>
    """, unsafe_allow_html=True)

st.header("EARRING COLLECTION")


def display_images(folder):
    image_files = os.listdir(folder)
    cols = st.columns(3)
    for idx, image in enumerate(image_files):
        with cols[idx % 3]:
            st.image(os.path.join(folder, image), use_container_width=True)

# --- Display earring images ---
display_images("images/er")
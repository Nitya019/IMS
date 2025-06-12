#-----------importing modules-------------------------------#
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
st.set_page_config(layout="wide")


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
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Earring Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1])  # wider gaps: 0.3 spacing columns

    for _, row in earring_df.iterrows():
        col_index = item_count % 3 * 2  # Use 0, 2, 4 for real columns

        with cols[col_index]:
            st.image(row['Image'], use_container_width =True)
            st.markdown(f"""
                <div style="font-family:serif; font-size:20px; line-height:1.6; margin-top:10px;">
                    <strong>Weight:</strong> {row['Weight']}<br>
                    <strong>Purity:</strong> {row['Purity']}<br>
                    <strong>ID:</strong> {row['UID']}
                </div>
            """, unsafe_allow_html=True)

        item_count += 1

        if item_count % 3 == 0:
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)  # more vertical gap
            cols = st.columns([1, 0.3, 1, 0.3, 1])  # reset with same wider spacing


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
    


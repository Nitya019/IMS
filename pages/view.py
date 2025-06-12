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
bg_df = df[df["Category"] == "Bangle"]
tk_df = df[df["Category"] == "Tika"]
pd_df = df[df["Category"] == "Pendant"]

#-------------functions for each product----------------------#
def ear_page():
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Earring Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1])  

    for _, row in earring_df.iterrows():
        col_index = item_count % 3 * 2 

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
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True) 
            cols = st.columns([1, 0.3, 1, 0.3, 1])  


def set_page():
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Set Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1]) 

    for _, row in set_df.iterrows():
        col_index = item_count % 3 * 2  

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
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)  
            cols = st.columns([1, 0.3, 1, 0.3, 1])  

def br_page():
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Bracelet Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1])  

    for _, row in brace_df.iterrows():
        col_index = item_count % 3 * 2  

        with cols[col_index]:
            st.image(row['Image'], width= 200 )
            st.markdown(f"""
                <div style="font-family:serif; font-size:20px; line-height:1.6; margin-top:10px;">
                    <strong>Weight:</strong> {row['Weight']}<br>
                    <strong>Purity:</strong> {row['Purity']}<br>
                    <strong>ID:</strong> {row['UID']}
                </div>
            """, unsafe_allow_html=True)

        item_count += 1

        if item_count % 3 == 0:
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True) 
            cols = st.columns([1, 0.3, 1, 0.3, 1]) 

def ms_page():
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Bracelet Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1]) 

    for _, row in ms_df.iterrows():
        col_index = item_count % 3 * 2  

        with cols[col_index]:
            st.image(row['Image'], width= 200 )
            st.markdown(f"""
                <div style="font-family:serif; font-size:20px; line-height:1.6; margin-top:10px;">
                    <strong>Weight:</strong> {row['Weight']}<br>
                    <strong>Purity:</strong> {row['Purity']}<br>
                    <strong>ID:</strong> {row['UID']}
                </div>
            """, unsafe_allow_html=True)

        item_count += 1

        if item_count % 3 == 0:
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)  
            cols = st.columns([1, 0.3, 1, 0.3, 1]) 

def bg_page():
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Bangle Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1])  

    for _, row in bg_df.iterrows():
        col_index = item_count % 3 * 2 

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
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True) 
            cols = st.columns([1, 0.3, 1, 0.3, 1])  

def tk_page():
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Tika Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1])  

    for _, row in tk_df.iterrows():
        col_index = item_count % 3 * 2 

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
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True) 
            cols = st.columns([1, 0.3, 1, 0.3, 1])  

def pd_page():
    st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f5f5dc; 
    font-family: Georgia, serif; text-shadow: 1px 1px 2px #333;'>Pendant Collection</h1>
    """, unsafe_allow_html=True)

    item_count = 0
    cols = st.columns([1, 0.3, 1, 0.3, 1])  

    for _, row in pd_df.iterrows():
        col_index = item_count % 3 * 2 

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
            st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True) 
            cols = st.columns([1, 0.3, 1, 0.3, 1])  



#----------------adding the sidebar-------------------------#
st.sidebar.title("Inventory")

opt = st.sidebar.selectbox(
    "Choose a product", ["Earrings", "Sets", "Bracelets", "Mangalsutra", "Bangles","Tika", "Pendants"]
)

if opt == "Earrings":
    ear_page()
    
if opt == "Sets":
    set_page()

if opt == "Bracelets":
    br_page()

if opt == "Mangalsutra":
    ms_page()
    
if opt == "Bangles":
    bg_page()
    
if opt == "Tika":
    tk_page()
    
if opt == "Pendants":
    pd_page()
    

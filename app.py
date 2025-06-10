import streamlit as st
from earring import show_earrings
from sets import show_sets

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigation buttons (only if no page selected or back on home)
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center;'>VN JEWELLERS</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Earrings"):
            st.session_state.page = "earring"
    with col2:
        if st.button("Set"):
            st.session_state.page = "set"

# Page Routing
if st.session_state.page == "earring":
    show_earrings()
elif st.session_state.page == "set":
    show_sets()

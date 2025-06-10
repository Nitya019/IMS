import streamlit as st
from earring import show_earrings
from set import show_sets  # if you have a "Set" section

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigation buttons
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
else:
    st.write("Welcome to VN Jewellers! Click a button to explore.")

df = pd.read_csv("data.csv")
cat = df["Category"] == "Set"
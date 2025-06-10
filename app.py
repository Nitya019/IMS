import streamlit as st



# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Page switch function
def go_to(page_name):
    st.session_state.page = page_name

# --- Navigation ---
st.markdown("""
<style>
.big-font {
    font-size:75px !important;
    color:white;
    text-align: center;
    font-family: 'Roboto', Monospace;
}
</style>
<div class="big-font">VN JEWELLERS</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Earrings"):
        go_to('earrings')

with col2:
    if st.button("Set"):
        go_to('set')

st.markdown("---")


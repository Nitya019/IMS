#-----------importing modules-------------------------------#
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

st.set_page_config(layout = "wide",
    page_title="Inventory System",
    page_icon="✨",
)
st.markdown("""
<style>
@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
}
.fancy-title {
    text-align: center;
    font-size: 70px;
    font-weight: bold;
    background: linear-gradient(90deg, #f8f1e4, #e6cc99, #f8f1e4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeIn 2s ease-in-out;
    margin-bottom: 10px;
}
</style>

<h1 class='fancy-title'>VN Jewellers</h1>
""", unsafe_allow_html=True)

st.markdown("""

    <h3 style='text-align: center; color: #e6cc99; font-weight: normal;'>
    A Legacy of Excellence from <strong><span style="font-size: 30px;">Munna Lal Verma Jewellers</span></strong>
    </h3>


    <p style='text-align: center; font-size: 18px; color: #c8bfae; padding: 20px 100px;'>
        At VN Jewellers, we blend <strong>50+ years of tradition</strong> with modern artistry to offer you timeless and elegant jewellery. 
        As a proud extension of <strong>Munna Lal Verma Jewellers</strong>, our commitment is to quality, authenticity, and customer trust.
        Explore our curated catalogue of craftsmanship that speaks of both heritage and innovation.
    </p>

    <br>
 
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2.2, 1])  # Adjust column widths for centering
with col2:
    st.image("images\S1.webp",width=600 )

if st.button("Go to Catalogue"):
    st.switch_page("pages/View.py")
st.markdown("""<div style='text-align: center; font-size:18px; color: #e6cc99;'>
        <strong>📍 VN Jewellers, Adonia Breeze Complex, Munshipulia Chauraha, Panigaon, Lucknow</strong><br>
        📞 +91 9918402555 &nbsp;&nbsp;&nbsp;&nbsp; 📞 +91 6393799551<br>
        📧 vnjewellers@example.com
    <br><br>
    <div style='text-align: left;'>
    </div>
""", unsafe_allow_html=True)
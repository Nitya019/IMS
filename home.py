#-----------importing modules-------------------------------#
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

st.set_page_config(layout = "wide",
    page_title="Inventory System",
    page_icon="✨",
)

st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #f8f1e4;'>VN Jewellers</h1>
    <h3 style='text-align: center; color: #e6cc99; font-weight: normal;'>
        A Legacy of Excellence from <strong>Munna Lal Verma Jewellers</strong>
    </h3>

    <p style='text-align: center; font-size: 18px; color: #c8bfae; padding: 20px 100px;'>
        At VN Jewellers, we blend <strong>50+ years of tradition</strong> with modern artistry to offer you timeless and elegant jewellery. 
        As a proud extension of <strong>Munna Lal Verma Jewellers</strong>, our commitment is to quality, authenticity, and customer trust.
        Explore our curated catalogue of craftsmanship that speaks of both heritage and innovation.
    </p>

    <br>
    <div style='text-align: center; font-size:18px; color: #e6cc99;'>
        <strong>📍 VN Jewellers, Adonia Breeze Complex, Munshipulia Chauraha, Panigaon, Lucknow</strong><br>
        📞 +91 9918402555 &nbsp;&nbsp;&nbsp;&nbsp; 📞 +91 6393799551<br>
        📧 vnjewellers@example.com
    </div>

    <br><br>
    <div style='text-align: center;'>
    </div>
""", unsafe_allow_html=True)


if st.button("Go to Catalogue"):
    st.switch_page("pages/View.py")
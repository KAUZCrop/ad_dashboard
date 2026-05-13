import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="Meta Ads Dashboard", page_icon="📊")
st.markdown("""
<style>
.block-container{padding:0!important;max-width:100%!important}
#MainMenu,footer,header{visibility:hidden}
.stApp{margin:0;padding:0}
</style>
""", unsafe_allow_html=True)

html_path = os.path.join(os.path.dirname(__file__), "dashboard.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1600, scrolling=True)
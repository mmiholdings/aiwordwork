import streamlit as st
import requests

st.title("WordWeaver AI")

text = st.text_area("Enter a sentence to analyze:")
if st.button("Analyze"):
    response = requests.post("http://localhost:8000/analyze", json={"text": text})
    st.json(response.json())

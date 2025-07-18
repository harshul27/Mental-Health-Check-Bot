import streamlit as st
from dotenv import load_dotenv
import os
from main import run_checkin_bot  # assuming main.py has the core logic

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

st.title("Mental Health Check-in Bot")

if st.button("Start Check-in"):
    response = run_checkin_bot(api_key=google_api_key)
    st.write(response)

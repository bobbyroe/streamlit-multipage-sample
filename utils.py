import streamlit as st

def initialize_session_state():
    if 'emoji' not in st.session_state:
        st.session_state.emoji = "🏠"
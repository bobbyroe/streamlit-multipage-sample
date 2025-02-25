import streamlit as st
from utils import initialize_session_state

st.title("Projects")
initialize_session_state()
st.sidebar.success("Selected Emoji: %s" % st.session_state.emoji)
import streamlit as st
from utils import initialize_session_state

st.title("Home")

initialize_session_state()
st.sidebar.success("Selected Emoji: %s" % st.session_state.emoji)

all_emojis = ["🏠", "🚀", "🔥", "🌈", "🦄"]
selected_index = all_emojis.index(st.session_state.emoji)
st.session_state.emoji = st.selectbox(
    "Selected Emoji",
    all_emojis,
    index=selected_index,
)
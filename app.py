# Task 4: Add session state to your app to maintain chat history.

import streamlit as st
st.title("AI Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def send_message():
    user_message = st.session_state.user_input
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})
        bot_response = f"{user_message}"
        st.session_state.messages.append({"role": "bot", "content": bot_response})
        st.session_state.user_input = ""



for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg['content'])
    else:
        with st.chat_message("assistant"):
            st.write(msg['content'])

st.text_input("You:", key="user_input", on_change=send_message, placeholder="Say Something")

import streamlit as st
from utils.ai_generator import travel_chat
from utils.translator import load_language

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Travel Assistant", page_icon="🤖", layout="wide")

# ----------------------------
# Language Setup
# ----------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

st.session_state.language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"],
    index=["English", "Hindi", "Telugu"].index(st.session_state.language),
    key="travel_language",
)

lang_map = {"English": "en", "Hindi": "hi", "Telugu": "te"}

text = load_language(lang_map[st.session_state.language])

# ----------------------------
# Title
# ----------------------------
st.title(text["travel_assistant"])

st.write(text["travel_assistant_description"])

st.markdown("---")

# ----------------------------
# Trip Context
# ----------------------------
destination = st.session_state.get("destination", text["unknown_destination"])
itinerary = st.session_state.get("itinerary", "")

st.info(f"{text['current_destination']}: {destination}")

# ----------------------------
# Initialize Chat History
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------
# Display Previous Messages
# ----------------------------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Chat Input
# ----------------------------
user_prompt = st.chat_input(text["chat_placeholder"])

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    with st.spinner(text["thinking"]):
        response = travel_chat(
            destination=destination, itinerary=itinerary, question=user_prompt
        )

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.chat_history.append({"role": "assistant", "content": response})

st.markdown("---")

# ----------------------------
# Suggested Questions
# ----------------------------
st.subheader(text["suggested_questions"])

col1, col2 = st.columns(2)

with col1:
    st.write(f"• {text['q1']}")
    st.write(f"• {text['q2']}")
    st.write(f"• {text['q3']}")
    st.write(f"• {text['q4']}")

with col2:
    st.write(f"• {text['q5']}")
    st.write(f"• {text['q6']}")
    st.write(f"• {text['q7']}")
    st.write(f"• {text['q8']}")

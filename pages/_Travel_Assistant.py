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

# Load translations
text = load_language(lang_map[st.session_state.language])

# ----------------------------
# DEBUG (Temporary)
# ----------------------------


# ----------------------------
# Title
# ----------------------------
st.title(text.get("travel_assistant", "🤖 AI Travel Assistant"))

st.write(
    text.get(
        "travel_assistant_description",
        (
            "Ask questions about your trip, destination, attractions, "
            "food, transportation, packing, weather, or travel tips."
        ),
    )
)

st.markdown("---")

# ----------------------------
# Trip Context
# ----------------------------
destination = st.session_state.get(
    "destination", text.get("unknown_destination", "Unknown Destination")
)

itinerary = st.session_state.get("itinerary", "")

st.info(f"{text.get('current_destination', 'Current Destination')}: {destination}")

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
user_prompt = st.chat_input(
    text.get("chat_placeholder", "Ask anything about your trip...")
)

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    with st.spinner(text.get("thinking", "Thinking...")):
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
st.subheader(text.get("suggested_questions", "💡 Suggested Questions"))

col1, col2 = st.columns(2)

with col1:
    st.write(f"• {text.get('q1', 'What should I pack?')}")
    st.write(f"• {text.get('q2', 'Best local food to try?')}")
    st.write(f"• {text.get('q3', 'Any hidden attractions?')}")
    st.write(f"• {text.get('q4', 'How can I save money?')}")

with col2:
    st.write(f"• {text.get('q5', 'Best time to visit?')}")
    st.write(f"• {text.get('q6', 'Local transportation options?')}")
    st.write(f"• {text.get('q7', 'Safety tips?')}")
    st.write(f"• {text.get('q8', 'Recommended restaurants?')}")

import streamlit as st
from utils.ai_generator import travel_chat

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Travel Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Travel Assistant")

st.write(
    """
    Ask questions about your trip, destination,
    attractions, food, transportation, packing,
    weather, or travel tips.
    """
)

st.markdown("---")

# ----------------------------
# Trip Context
# ----------------------------
destination = st.session_state.get(
    "destination",
    "Unknown Destination"
)

itinerary = st.session_state.get(
    "itinerary",
    ""
)

st.info(f"Current Destination: {destination}")

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
    "Ask anything about your trip..."
)

if user_prompt:

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Generate AI Response
    with st.spinner("Thinking..."):

        response = travel_chat(
            destination=destination,
            itinerary=itinerary,
            question=user_prompt
        )

    # Display Assistant Message
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response
        }
    )

st.markdown("---")

# ----------------------------
# Suggested Questions
# ----------------------------
st.subheader("💡 Suggested Questions")

col1, col2 = st.columns(2)

with col1:
    st.write("• What should I pack?")
    st.write("• Best local food to try?")
    st.write("• Any hidden attractions?")
    st.write("• How can I save money?")

with col2:
    st.write("• Best time to visit?")
    st.write("• Local transportation options?")
    st.write("• Safety tips?")
    st.write("• Recommended restaurants?")
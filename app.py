import streamlit as st

from agent.agent import travel_agent
from utils.translator import load_language

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
)

# ----------------------------
# Language Selection
# ----------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

st.session_state.language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"],
    index=["English", "Hindi", "Telugu"].index(st.session_state.language),
    key="app_language",
)

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
}

text = load_language(lang_map[st.session_state.language])

# ----------------------------
# Main Page
# ----------------------------
st.title(text["app_title"])

st.markdown(
    f"""
## {text["welcome_heading"]}

{text["welcome_description"]}

### {text["features_heading"]}

- 🗺️ {text["feature_trip_planner"]}
- 💰 {text["feature_budget_tracker"]}
- 🤖 {text["feature_travel_assistant"]}
- 📄 {text["feature_pdf"]}
- 📍 {text["feature_maps"]}

{text["sidebar_navigation"]}
"""
)

st.success(text["select_page"])

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        f"""
### 🗺️ {text["trip_planner"]}

{text["trip_planner_info"]}
"""
    )

with col2:
    st.info(
        f"""
### 💰 {text["budget_tracker"]}

{text["budget_tracker_info"]}
"""
    )

with col3:
    st.info(
        f"""
### 🤖 {text["travel_assistant"]}

{text["travel_assistant_info"]}
"""
    )

st.markdown("---")
st.subheader("🤖 AI Travel Agent (ADK Demo)")

user_query = st.text_input(
    "Ask the Travel Agent",
    placeholder="Plan a 4-day trip to Goa under ₹15,000",
)

if st.button("Run Agent"):
    if user_query:
        with st.spinner("Agent is thinking..."):
            try:
                result = travel_agent.run(user_query)
                st.success("Agent Response")
                st.write(result)
            except Exception as e:
                st.error(f"Agent Error: {e}")
 (Fix pylint errors and travel agent imports)
st.caption(text["app_footer"])

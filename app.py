import streamlit as st
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

st.caption(text["app_footer"])

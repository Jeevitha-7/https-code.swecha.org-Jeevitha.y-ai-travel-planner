import streamlit as st
from utils.ai_generator import generate_itinerary
from utils.budget_calculator import calculate_budget
from utils.translator import load_language


# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Trip Planner",
    page_icon="🗺️",
    layout="wide",
)

# ----------------------------
# Language Setup
# ----------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
}


# ----------------------------
# Language Selection
# ----------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

st.session_state.language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"],
    index=["English", "Hindi", "Telugu"].index(st.session_state.language),
    key="trip_language",
)

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
}

text = load_language(lang_map[st.session_state.language])

text = load_language(lang_map[st.session_state.language])

# ----------------------------
# Title
# ----------------------------
st.title(text["trip_planner_title"])
st.write(text["trip_planner_description"])

# ----------------------------
# Inputs
# ----------------------------
destination = st.text_input(text["destination"])

budget = st.number_input(
    text["budget"],
    min_value=1000,
    value=10000,
)

days = st.number_input(
    text["days"],
    min_value=1,
    value=3,
)

travelers = st.number_input(
    text["travelers"],
    min_value=1,
    value=1,
)

travel_style = st.selectbox(
    text["travel_style"],
    [
        text["budget_style"],
        text["standard_style"],
        text["luxury_style"],
    ],
)

interests = st.multiselect(
    text["interests"],
    [
        text["adventure"],
        text["food_interest"],
        text["nature"],
        text["historical"],
        text["shopping_interest"],
        text["beaches"],
        text["wildlife"],
        text["photography"],
    ],
)

# ----------------------------
# AI Provider
# ----------------------------
if "ai_provider" not in st.session_state:
    st.session_state.ai_provider = "Gemini"

st.session_state.ai_provider = st.sidebar.selectbox(
    text["ai_provider"],
    ["Gemini", "Ollama"],
    index=["Gemini", "Ollama"].index(st.session_state.ai_provider),
)

# ----------------------------
# Generate Button
# ----------------------------
if st.button(text["generate_itinerary_btn"]):
    if not destination:
        st.error(text["enter_destination"])
        st.stop()

    budget_data = calculate_budget(budget, days)

    itinerary = generate_itinerary(
        destination=destination,
        budget=budget,
        days=days,
        travelers=travelers,
        travel_style=travel_style,
        interests=interests,
        language=st.session_state.language,
    )

    st.session_state["budget"] = budget
    st.session_state["itinerary"] = itinerary
    st.session_state["destination"] = destination

    st.success(text["trip_generated"])

    # ----------------------------
    # Budget Breakdown
    # ----------------------------
    st.subheader(text["budget_breakdown"])

    st.write(f"{text['transport']}: ₹{budget_data}")
    st.write(f"{text['hotel']}: ₹{budget_data}")
    st.write(f"{text['food']}: ₹{budget_data}")
    st.write(f"{text['activities']}: ₹{budget_data}")

    # ----------------------------
    # Itinerary
    # ----------------------------
    st.subheader(text["generated_itinerary"])

    st.markdown(itinerary)

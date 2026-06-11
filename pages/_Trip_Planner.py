import streamlit as st
from utils.ai_generator import generate_itinerary
from utils.budget_calculator import calculate_budget

st.set_page_config(
    page_title="Trip Planner",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ AI Trip Planner")
st.write("Generate a personalized travel itinerary using AI.")

destination = st.text_input("📍 Destination")

budget = st.number_input(
    "💰 Budget (₹)",
    min_value=1000,
    value=10000
)

days = st.number_input(
    "📅 Number of Days",
    min_value=1,
    value=3
)

travelers = st.number_input(
    "👥 Number of Travelers",
    min_value=1,
    value=1
)

travel_style = st.selectbox(
    "✨ Travel Style",
    ["Budget", "Standard", "Luxury"]
)

interests = st.multiselect(
    "🎯 Interests",
    [
        "Adventure",
        "Food",
        "Nature",
        "Historical",
        "Shopping",
        "Beaches",
        "Wildlife",
        "Photography"
    ]
)

if st.button("🚀 Generate Itinerary"):

    budget_data = calculate_budget(budget)

    itinerary = generate_itinerary(
        destination=destination,
        budget=budget,
        days=days,
        travelers=travelers,
        travel_style=travel_style,
        interests=interests
    )

    st.session_state["budget"] = budget
    st.session_state["itinerary"] = itinerary
    st.session_state["destination"] = destination

    st.success("Trip generated successfully!")

    st.subheader("💰 Budget Breakdown")

    st.write(f"Transport: ₹{budget_data['transport']}")
    st.write(f"Hotel: ₹{budget_data['hotel']}")
    st.write(f"Food: ₹{budget_data['food']}")
    st.write(f"Activities: ₹{budget_data['activities']}")

    st.subheader("🗺️ AI Generated Itinerary")

    st.markdown(itinerary)
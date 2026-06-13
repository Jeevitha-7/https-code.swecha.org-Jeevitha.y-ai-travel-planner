import streamlit as st
from utils.ai_generator import generate_itinerary
from utils.budget_calculator import calculate_budget

st.set_page_config(page_title="Trip Planner", page_icon="🗺️", layout="wide")

st.title("🗺️ AI Trip Planner")
st.write("Generate a personalized travel itinerary using AI.")

# ---------------- Inputs ----------------
destination = st.text_input("📍 Destination")

budget = st.number_input("💰 Budget (₹)", min_value=1000, value=10000)

days = st.number_input("📅 Number of Days", min_value=1, value=3)

travelers = st.number_input("👥 Number of Travelers", min_value=1, value=1)

travel_style = st.selectbox("✨ Travel Style", ["Budget", "Standard", "Luxury"])

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
        "Photography",
    ],
)

# ---------------- Button ----------------
if st.button("🚀 Generate Itinerary"):
    if not destination:
        st.error("Please enter destination")
        st.stop()

    # FIXED function call
    budget_data = calculate_budget(budget, days)

    # FIXED variables (no undefined names)
    itinerary = generate_itinerary(
        destination, budget, days, travelers, travel_style.lower(), interests
    )

    # Save in session
    st.session_state["budget"] = budget
    st.session_state["itinerary"] = itinerary
    st.session_state["destination"] = destination

    st.success("Trip generated successfully!")

    # ---------------- Budget ----------------
    st.subheader("💰 Budget Breakdown")

    st.write(f"Transport: ₹{budget_data}")
    st.write(f"Hotel: ₹{budget_data}")
    st.write(f"Food: ₹{budget_data}")
    st.write(f"Activities: ₹{budget_data}")

    # ---------------- Itinerary ----------------
    st.subheader("🗺️ AI Generated Itinerary")
    st.markdown(itinerary)

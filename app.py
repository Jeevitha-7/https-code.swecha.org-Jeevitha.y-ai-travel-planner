import streamlit as st
from utils.ai_generator import generate_itinerary
from utils.budget_calculator import allocate_budget

# Page Configuration
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# Load Custom CSS
try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# Sidebar
try:
    st.sidebar.image("assets/logo.png", width=150)
except:
    pass

st.sidebar.title("✈️ AI Travel Planner")
st.sidebar.write(
    "Plan your perfect trip with AI based on your budget and interests."
)

# Banner
try:
    st.image("assets/banner.jpg", use_container_width=True)
except:
    pass

# Main Title
st.title("🌍 AI Travel Planner")
st.markdown(
    "Enter your travel details and get a personalized itinerary."
)

# User Inputs
col1, col2 = st.columns(2)

with col1:
    destination = st.text_input(
        "📍 Destination",
        placeholder="e.g., Goa"
    )

    budget = st.number_input(
        "💰 Budget (₹)",
        min_value=1000,
        value=10000,
        step=1000
    )

with col2:
    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=3
    )

    style = st.selectbox(
        "🏨 Travel Style",
        ["Budget", "Standard", "Luxury"]
    )

interests = st.multiselect(
    "🎯 Interests",
    [
        "Adventure",
        "Food",
        "Nature",
        "Shopping",
        "Historical Places",
        "Beaches",
        "Wildlife",
        "Photography"
    ]
)

# Generate Button
if st.button("🚀 Generate Travel Plan"):

    if not destination:
        st.warning("Please enter a destination.")
        st.stop()

    # Budget Breakdown
    st.subheader("💰 Budget Breakdown")

    allocation = allocate_budget(budget)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Travel",
            f"₹{allocation['Travel']:.0f}"
        )

    with col2:
        st.metric(
            "Hotel",
            f"₹{allocation['Hotel']:.0f}"
        )

    with col3:
        st.metric(
            "Food",
            f"₹{allocation['Food']:.0f}"
        )

    with col4:
        st.metric(
            "Activities",
            f"₹{allocation['Activities']:.0f}"
        )

    st.divider()

    # Generate AI Itinerary
    with st.spinner("Generating your personalized travel plan..."):

        itinerary = generate_itinerary(
            destination=destination,
            budget=budget,
            days=days,
            interests=", ".join(interests),
            style=style
        )

    st.subheader("🗺️ Your AI Travel Itinerary")

    st.markdown(itinerary)

    st.success("Travel plan generated successfully!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Gemini AI")
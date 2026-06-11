import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Home | AI Travel Planner", page_icon="🏠", layout="wide")

# ----------------------------
# Hero Section
# ----------------------------
st.title("✈️ AI Travel Planner")

st.markdown(
    """
    ## Plan Smarter. Travel Better.

    Welcome to **AI Travel Planner**, your intelligent travel companion.

    Generate personalized travel itineraries, optimize your budget,
    discover attractions, check weather forecasts, and download
    professional trip reports — all in one place.
    """
)

st.markdown("---")

# ----------------------------
# Features Section
# ----------------------------
st.header("🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
        ### 🗺️ AI Itinerary Generator

        Generate complete day-wise travel plans based on:

        - Destination
        - Budget
        - Duration
        - Interests
        """
    )

with col2:
    st.info(
        """
        ### 💰 Budget Planning

        Smart budget allocation for:

        - Transport
        - Hotels
        - Food
        - Activities
        """
    )

with col3:
    st.info(
        """
        ### 🤖 Travel Assistant

        Ask questions such as:

        - Best places to visit?
        - Local food recommendations?
        - Hidden attractions?
        """
    )

st.markdown("---")

# ----------------------------
# How It Works
# ----------------------------
st.header("📍 How It Works")

step1, step2, step3 = st.columns(3)

with step1:
    st.success(
        """
        ### Step 1

        Enter:

        - Destination
        - Budget
        - Days
        - Travelers
        """
    )

with step2:
    st.success(
        """
        ### Step 2

        Select:

        - Travel Style
        - Interests
        - Preferences
        """
    )

with step3:
    st.success(
        """
        ### Step 3

        AI generates:

        - Itinerary
        - Budget Plan
        - Travel Tips
        """
    )

st.markdown("---")

# ----------------------------
# Statistics
# ----------------------------
st.header("📊 Travel Insights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Destinations", "100+")

with col2:
    st.metric("Trips Planned", "1000+")

with col3:
    st.metric("Countries", "50+")

with col4:
    st.metric("AI Accuracy", "95%")

st.markdown("---")

# ----------------------------
# Popular Destinations
# ----------------------------
st.header("🌍 Popular Destinations")

dest1, dest2, dest3 = st.columns(3)

with dest1:
    st.card = st.container()
    with st.card:
        st.subheader("🏖️ Goa")
        st.write("Beaches, nightlife, water sports, seafood.")

with dest2:
    st.card = st.container()
    with st.card:
        st.subheader("🏔️ Manali")
        st.write("Mountains, adventure sports, scenic beauty.")

with dest3:
    st.card = st.container()
    with st.card:
        st.subheader("🏰 Jaipur")
        st.write("Forts, palaces, culture, heritage sites.")

st.markdown("---")

# ----------------------------
# Quick Navigation
# ----------------------------
st.header("📌 Start Planning")

st.write(
    """
    Use the navigation menu in the sidebar to access:

    - 🗺️ Trip Planner
    - 💰 Budget Tracker
    - 🤖 Travel Assistant
    """
)

st.success(
    "Click on 'Trip Planner' from the sidebar to generate your first AI-powered travel itinerary."
)

st.markdown("---")

# ----------------------------
# Footer
# ----------------------------
st.caption(
    "AI Travel Planner • Built with Streamlit, Gemini AI, Weather APIs, and Interactive Maps"
)

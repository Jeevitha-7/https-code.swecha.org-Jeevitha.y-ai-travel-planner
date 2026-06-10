import streamlit as st
from pathlib import Path

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Load Custom CSS
# ----------------------------
css_file = Path("assets/styles.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("✈️ AI Travel Planner")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Plan your trips with AI.

    Features:
    - AI Itinerary Generator
    - Budget Planner
    - Travel Assistant
    - Weather Information
    - PDF Reports
    """
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Use the navigation menu above to explore the app."
)

# ----------------------------
# Main Page
# ----------------------------
st.title("✈️ AI Travel Planner")

st.markdown(
    """
    ### Plan Your Dream Trip in Seconds

    AI Travel Planner helps you create personalized travel itineraries
    based on your destination, budget, trip duration, and interests.

    Generate:
    - 🗺️ Day-wise Travel Plans
    - 💰 Budget Allocation
    - 🌤️ Weather Insights
    - 📄 Downloadable PDF Reports
    - 🤖 AI Travel Assistance
    """
)

# ----------------------------
# Hero Section
# ----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Why Use AI Travel Planner?")

    st.write(
        """
        Planning a trip can be time-consuming.

        Our AI assistant creates complete itineraries
        tailored to your preferences, helping you save
        time and stay within budget.
        """
    )

with col2:
    st.metric("Trips Planned", "100+")
    st.metric("Destinations", "50+")
    st.metric("Happy Travelers", "500+")

st.markdown("---")

# ----------------------------
# Features
# ----------------------------
st.header("🚀 Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.info(
        """
        ### 🗺️ Trip Planner

        Generate detailed day-wise travel itineraries
        using AI.
        """
    )

with feature2:
    st.info(
        """
        ### 💰 Budget Tracker

        Allocate and monitor your travel expenses.
        """
    )

with feature3:
    st.info(
        """
        ### 🤖 Travel Assistant

        Ask travel-related questions and get
        instant AI-powered answers.
        """
    )

st.markdown("---")

# ----------------------------
# Quick Start
# ----------------------------
st.header("📍 Quick Start")

st.write(
    """
    1. Open **Trip Planner** from the sidebar.
    2. Enter your destination.
    3. Set your budget and trip duration.
    4. Select your interests.
    5. Click Generate Trip.
    """
)

st.success(
    "Navigate to 'Trip Planner' from the sidebar to start planning your trip."
)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit, Gemini AI, OpenWeather API, and Folium."
)
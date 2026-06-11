import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

# ----------------------------
# Main Page
# ----------------------------
st.title("✈️ AI Travel Planner")

st.markdown("""
## Welcome to AI Travel Planner

Plan your trips using AI.

### Features
- 🗺️ AI Trip Planner
- 💰 Budget Tracker
- 🤖 Travel Assistant
- 📄 PDF Download
- 📍 Destination Maps

Use the sidebar to navigate through the application.
""")

st.success("Select a page from the sidebar to get started.")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 🗺️ Trip Planner

    Generate day-wise itineraries
    using Gemini AI.
    """)

with col2:
    st.info("""
    ### 💰 Budget Tracker

    Track travel expenses
    and spending.
    """)

with col3:
    st.info("""
    ### 🤖 Travel Assistant

    Ask questions about
    your destination.
    """)

st.markdown("---")

st.caption("Built with ❤️ using Streamlit and Gemini AI")

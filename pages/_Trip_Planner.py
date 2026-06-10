import streamlit as st
from utils.ai_generator import generate_itinerary
from utils.budget_calculator import calculate_budget
from utils.pdf_generator import generate_pdf

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Trip Planner",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ AI Trip Planner")
st.write("Generate a personalized travel itinerary using AI.")

st.markdown("---")

# ----------------------------
# User Inputs
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    destination = st.text_input(
        "📍 Destination",
        placeholder="Goa"
    )

    budget = st.number_input(
        "💰 Budget (₹)",
        min_value=1000,
        step=1000
    )

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=3
    )

with col2:
    travelers = st.number_input(
        "👥 Number of Travelers",
        min_value=1,
        value=1
    )

    travel_style = st.selectbox(
        "✨ Travel Style",
        [
            "Budget",
            "Standard",
            "Luxury"
        ]
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

st.markdown("---")

# ----------------------------
# Generate Button
# ----------------------------
if st.button("🚀 Generate Itinerary", use_container_width=True):

    if not destination:
        st.error("Please enter a destination.")
        st.stop()

    with st.spinner("Generating your trip plan..."):

        # Budget Allocation
        budget_data = calculate_budget(budget)

        # AI Itinerary
        itinerary = generate_itinerary(
            destination=destination,
            budget=budget,
            days=days,
            travelers=travelers,
            travel_style=travel_style,
            interests=interests
        )

    st.success("Trip Plan Generated Successfully!")

    st.markdown("---")

    # ----------------------------
    # Trip Summary
    # ----------------------------
    st.header("📋 Trip Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Destination", destination)
    col2.metric("Budget", f"₹{budget:,}")
    col3.metric("Days", days)
    col4.metric("Travelers", travelers)

    st.markdown("---")

    # ----------------------------
    # Budget Breakdown
    # ----------------------------
    st.header("💰 Budget Allocation")

    b1, b2, b3, b4 = st.columns(4)

    b1.metric("Transport", f"₹{budget_data['transport']:,}")
    b2.metric("Hotel", f"₹{budget_data['hotel']:,}")
    b3.metric("Food", f"₹{budget_data['food']:,}")
    b4.metric("Activities", f"₹{budget_data['activities']:,}")

    st.markdown("---")

    # ----------------------------
    # AI Generated Itinerary
    # ----------------------------
    st.header("🗺️ AI Generated Itinerary")

    st.markdown(itinerary)

    st.markdown("---")

    # ----------------------------
    # PDF Download
    # ----------------------------
    pdf_file = generate_pdf(
        destination=destination,
        budget=budget,
        days=days,
        travelers=travelers,
        itinerary=itinerary
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name=f"{destination}_trip_plan.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.markdown("---")

    # ----------------------------
    # Travel Tips
    # ----------------------------
    st.header("💡 Travel Tips")

    st.info(
        """
        • Book accommodations early.

        • Keep emergency contacts handy.

        • Carry essential documents.

        • Research local transportation options.

        • Keep some extra budget for unexpected expenses.
        """
    )

    st.markdown("---")

    # ----------------------------
    # Save in Session State
    # ----------------------------
    st.session_state["destination"] = destination
    st.session_state["budget"] = budget
    st.session_state["days"] = days
    st.session_state["itinerary"] = itinerary

else:

    st.info(
        """
        Fill in your trip details and click
        **Generate Itinerary** to get started.
        """
    )
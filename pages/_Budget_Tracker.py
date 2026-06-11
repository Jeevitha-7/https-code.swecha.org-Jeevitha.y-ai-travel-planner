import streamlit as st
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Budget Tracker", page_icon="💰", layout="wide")

st.title("💰 Travel Budget Tracker")

st.write("Track your travel expenses and monitor your remaining budget.")

st.markdown("---")

# ----------------------------
# Get Budget from Session
# ----------------------------
if "budget" not in st.session_state:
    st.warning(
        "No trip budget found.\n\n"
        "Please generate a trip first from the Trip Planner page."
    )
    st.stop()

total_budget = st.session_state["budget"]

# ----------------------------
# Initialize Expenses
# ----------------------------
if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

# ----------------------------
# Budget Summary
# ----------------------------
spent = sum(expense["amount"] for expense in st.session_state["expenses"])

remaining = total_budget - spent

col1, col2, col3 = st.columns(3)

col1.metric("Total Budget", f"₹{total_budget:,.0f}")

col2.metric("Spent", f"₹{spent:,.0f}")

col3.metric("Remaining", f"₹{remaining:,.0f}")

st.markdown("---")

# ----------------------------
# Add Expense
# ----------------------------
st.header("➕ Add Expense")

with st.form("expense_form"):
    category = st.selectbox(
        "Category", ["Transport", "Hotel", "Food", "Shopping", "Activities", "Other"]
    )

    amount = st.number_input("Amount (₹)", min_value=0.0, step=100.0)

    description = st.text_input("Description")

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        st.session_state["expenses"].append(
            {"category": category, "amount": amount, "description": description}
        )

        st.success("Expense Added Successfully!")

st.markdown("---")

# ----------------------------
# Expense History
# ----------------------------
st.header("📋 Expense History")

if st.session_state["expenses"]:
    df = pd.DataFrame(st.session_state["expenses"])

    st.dataframe(df, use_container_width=True)

else:
    st.info("No expenses added yet.")

st.markdown("---")

# ----------------------------
# Expense Breakdown
# ----------------------------
st.header("📊 Expense Breakdown")

if st.session_state["expenses"]:
    df = pd.DataFrame(st.session_state["expenses"])

    category_totals = df.groupby("category")["amount"].sum().reset_index()

    st.bar_chart(category_totals.set_index("category"))

else:
    st.info("Add some expenses to see charts.")

st.markdown("---")

# ----------------------------
# Budget Status
# ----------------------------
st.header("🚦 Budget Status")

usage_percentage = spent / total_budget * 100 if total_budget > 0 else 0

st.progress(min(int(usage_percentage), 100))

st.write(f"Budget Used: {usage_percentage:.1f}%")

if usage_percentage < 50:
    st.success("Excellent! You're within budget.")
elif usage_percentage < 80:
    st.warning("Keep an eye on your spending.")
elif usage_percentage <= 100:
    st.error("Budget is almost exhausted.")
else:
    st.error("You have exceeded your budget!")

st.markdown("---")

# ----------------------------
# Clear Expenses
# ----------------------------
if st.button("🗑️ Clear All Expenses", use_container_width=True):
    st.session_state["expenses"] = []
    st.rerun()

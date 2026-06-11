import streamlit as st
import pandas as pd
from utils.translator import load_language

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Budget Tracker", page_icon="💰", layout="wide")

# ----------------------------
# Language Setup
# ----------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

st.session_state.language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"],
    index=["English", "Hindi", "Telugu"].index(st.session_state.language),
    key="language_selector_budget",
)

lang_map = {"English": "en", "Hindi": "hi", "Telugu": "te"}

text = load_language(lang_map[st.session_state.language])

# ----------------------------
# Title
# ----------------------------
st.title(text["budget_tracker"])

st.write(text["budget_description"])

st.markdown("---")

# ----------------------------
# Get Budget
# ----------------------------
if "budget" not in st.session_state:
    st.warning(text["no_budget"])
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

with col1:
    st.metric(text["total_budget"], f"₹{total_budget:,.0f}")

with col2:
    st.metric(text["spent"], f"₹{spent:,.0f}")

with col3:
    st.metric(text["remaining"], f"₹{remaining:,.0f}")

st.markdown("---")

# ----------------------------
# Add Expense
# ----------------------------
st.header(text["add_expense"])

with st.form("expense_form"):
    category = st.selectbox(
        text["category"],
        [
            text["transport"],
            text["hotel"],
            text["food"],
            text["shopping"],
            text["activities"],
            text["other"],
        ],
    )

    amount = st.number_input(text["amount"], min_value=0.0, step=100.0)

    description = st.text_input(text["description"])

    submitted = st.form_submit_button(text["add_expense_btn"])

    if submitted:
        st.session_state["expenses"].append(
            {"category": category, "amount": amount, "description": description}
        )

        st.success(text["expense_added"])

st.markdown("---")

# ----------------------------
# Expense History
# ----------------------------
st.header(text["expense_history"])

if st.session_state["expenses"]:
    df = pd.DataFrame(st.session_state["expenses"])

    st.dataframe(df, use_container_width=True)

else:
    st.info(text["no_expenses"])

st.markdown("---")

# ----------------------------
# Expense Breakdown
# ----------------------------
st.header(text["expense_breakdown"])

if st.session_state["expenses"]:
    df = pd.DataFrame(st.session_state["expenses"])

    category_totals = df.groupby("category")["amount"].sum().reset_index()

    st.bar_chart(category_totals.set_index("category"))

else:
    st.info(text["add_expense_chart"])

st.markdown("---")

# ----------------------------
# Budget Status
# ----------------------------
st.header(text["budget_status"])

usage_percentage = spent / total_budget * 100 if total_budget > 0 else 0

st.progress(min(int(usage_percentage), 100))

st.write(f"{text['budget_used']} {usage_percentage:.1f}%")

if usage_percentage < 50:
    st.success(text["excellent"])

elif usage_percentage < 80:
    st.warning(text["keep_eye"])

elif usage_percentage <= 100:
    st.error(text["almost_exhausted"])

else:
    st.error(text["budget_exceeded"])

st.markdown("---")

# ----------------------------
# Clear Expenses
# ----------------------------
if st.button(text["clear_expenses"], use_container_width=True):
    st.session_state["expenses"] = []

    st.rerun()

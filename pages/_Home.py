import streamlit as st
from utils.translator import load_language

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Home | AI Travel Planner", page_icon="🏠", layout="wide")

# ----------------------------
# Language Selection
# ----------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"],
    index=["English", "Hindi", "Telugu"].index(st.session_state.language),
)

st.session_state.language = language

lang_map = {"English": "en", "Hindi": "hi", "Telugu": "te"}

text = load_language(lang_map[language])

# ----------------------------
# Hero Section
# ----------------------------
st.title(text["title"])

st.markdown(
    f"""
    ## {text["hero_heading"]}

    {text["hero_description"]}
    """
)

st.markdown("---")

# ----------------------------
# Features Section
# ----------------------------
st.header(text["features"])

col1, col2, col3 = st.columns(3)

with col1:
    st.info(text["feature1"])

with col2:
    st.info(text["feature2"])

with col3:
    st.info(text["feature3"])

st.markdown("---")

# ----------------------------
# How It Works
# ----------------------------
st.header(text["how_it_works"])

step1, step2, step3 = st.columns(3)

with step1:
    st.success(text["step1"])

with step2:
    st.success(text["step2"])

with step3:
    st.success(text["step3"])

st.markdown("---")

# ----------------------------
# Statistics
# ----------------------------
st.header(text["travel_insights"])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(text["destinations"], "100+")

with col2:
    st.metric(text["trips"], "1000+")

with col3:
    st.metric(text["countries"], "50+")

with col4:
    st.metric(text["accuracy"], "95%")

st.markdown("---")

# ----------------------------
# Popular Destinations
# ----------------------------
st.header(text["popular_destinations"])

dest1, dest2, dest3 = st.columns(3)

with dest1:
    with st.container():
        st.subheader("🏖️ Goa")
        st.write(text["goa"])

with dest2:
    with st.container():
        st.subheader("🏔️ Manali")
        st.write(text["manali"])

with dest3:
    with st.container():
        st.subheader("🏰 Jaipur")
        st.write(text["jaipur"])

st.markdown("---")

# ----------------------------
# Quick Navigation
# ----------------------------
st.header(text["start_planning"])

st.write(text["navigation"])

st.success(text["sidebar_message"])

st.markdown("---")

# ----------------------------
# Footer
# ----------------------------
st.caption(text["footer"])

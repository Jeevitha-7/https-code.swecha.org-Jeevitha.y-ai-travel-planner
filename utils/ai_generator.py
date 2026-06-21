import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from ollama import chat

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

# -----------------------------
# BYOK (Bring Your Own Key)
# -----------------------------
gemini_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password",
    help="Enter your own Gemini API Key to use AI features.",
)


# -----------------------------
# Gemini API helper
# -----------------------------
def _get_gemini_client():
    api_key = gemini_key or os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Please enter a Gemini API Key.")

    return genai.Client(api_key=api_key)


# -----------------------------
# Ollama Function
# -----------------------------
def generate_with_ollama(prompt):
    """
    Generate response using local Ollama model.
    Make sure 'ollama serve' is running.
    """

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]


# -----------------------------
# Generate Travel Itinerary
# -----------------------------
def generate_itinerary(
    destination,
    budget,
    days,
    travelers,
    travel_style,
    interests,
    language="English",
):
    """
    Generate AI-powered travel itinerary using
    Gemini or Ollama.
    """

    prompt = f"""
You are an expert travel planner.

Generate a complete {days}-day travel itinerary.

Destination: {destination}
Budget: ₹{budget}
Number of Travelers: {travelers}
Travel Style: {travel_style}
Interests: {", ".join(interests)}

IMPORTANT:
- Respond ONLY in {language}
- Include:
1. Day-wise itinerary
2. Places to visit
3. Food recommendations
4. Estimated expenses
5. Transportation suggestions
6. Travel tips
7. Best time to visit
8. Safety tips
"""

    provider = st.session_state.get("ai_provider", "Gemini")

    # Ollama
    if provider == "Ollama":
        try:
            return generate_with_ollama(prompt)
        except Exception as e:
            return f"❌ Ollama error generating itinerary:\n{e}"

    # Gemini
    try:
        client = _get_gemini_client()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"❌ Gemini error generating itinerary:\n{e}"


# -----------------------------
# Basic Placeholder
# -----------------------------
def generate_plan(destination, days):
    return {
        "destination": destination,
        "days": days,
        "plan": [],
    }


# -----------------------------
# Travel Assistant Chat
# -----------------------------
def travel_chat(destination, question, itinerary=None):
    """
    AI Travel Assistant.
    Uses Gemini or Ollama.
    """

    prompt = f"""
You are an expert travel assistant.

Destination:
{destination}

Existing Itinerary:
{itinerary if itinerary else "No itinerary available."}

User Question:
{question}

Answer clearly and helpfully.
"""

    provider = st.session_state.get("ai_provider", "Gemini")

    # Ollama
    if provider == "Ollama":
        try:
            return generate_with_ollama(prompt)
        except Exception as e:
            return f"❌ Ollama error:\n{e}"

    # Gemini
    try:
        client = _get_gemini_client()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"❌ Gemini error:\n{e}"

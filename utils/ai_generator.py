import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from ollama import chat

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()


# Gemini API helper
def _get_gemini_client():
    """Return a configured genai.Client or raise a clear error if API key missing."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Please set GEMINI_API_KEY in your environment or .env file."
        )

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
    Gemini or Ollama based on sidebar selection.
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

    # Use Ollama if explicitly selected
    if provider == "Ollama":
        try:
            return generate_with_ollama(prompt)
        except Exception as e:
            return f"❌ Ollama error generating itinerary:\n{e}"

    # Use Gemini when selected (or default)
    if provider == "Gemini":
        try:
            client = _get_gemini_client()
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            return f"❌ Gemini error generating itinerary:\n{e}"

    # Unknown provider: try Gemini first, then Ollama as a fallback
    try:
        client = _get_gemini_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception:
        try:
            return generate_with_ollama(prompt)
        except Exception as e:
            return f"❌ Error generating itinerary:\n{e}"


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

    # Ollama explicitly
    if provider == "Ollama":
        try:
            return generate_with_ollama(prompt)
        except Exception as e:
            return f"❌ Ollama error:\n{e}"

    # Gemini explicitly
    if provider == "Gemini":
        try:
            client = _get_gemini_client()
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            return f"❌ Gemini error:\n{e}"

    # Unknown provider: try Gemini then Ollama
    try:
        client = _get_gemini_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception:
        try:
            return generate_with_ollama(prompt)
        except Exception as e:
            return f"❌ Error:\n{e}"

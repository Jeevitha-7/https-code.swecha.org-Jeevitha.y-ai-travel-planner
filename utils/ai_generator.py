import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)


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
    Generate an AI-powered travel itinerary.
    """

    try:
        prompt = f"""
You are an expert travel planner.

Generate a complete {days}-day travel itinerary.

Destination: {destination}
Budget: ₹{budget}
Number of Travelers: {travelers}
Travel Style: {travel_style}
Interests: {", ".join(interests)}

IMPORTANT:
- Respond ONLY in {language}.
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

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"❌ Error generating itinerary: {e}"


def generate_plan(destination, days):
    """
    Basic placeholder plan.
    """
    return {
        "destination": destination,
        "days": days,
        "plan": [],
    }


def travel_chat(destination, question, itinerary=None):
    """
    AI Travel Assistant chat.
    """

    try:
        prompt = f"""
You are an expert travel assistant.

Destination:
{destination}

Itinerary:
{itinerary if itinerary else "No itinerary available."}

User Question:
{question}

Answer clearly and helpfully.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"❌ Error: {e}"

import os
from dotenv import load_dotenv
import google.generativeai as genai

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

# ----------------------------
# Configure Gemini
# ----------------------------
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )
else:
    model = None


# ----------------------------
# Generate Itinerary
# ----------------------------
def generate_itinerary(
    destination,
    budget,
    days,
    travelers,
    travel_style,
    interests
):
    if model is None:
        return "❌ Gemini API key not found. Check your .env file."

    prompt = f"""
    Create a detailed travel itinerary.

    Destination: {destination}
    Budget: ₹{budget}
    Days: {days}
    Travelers: {travelers}
    Travel Style: {travel_style}
    Interests: {", ".join(interests)}

    Include:
    - Day-wise itinerary
    - Places to visit
    - Food recommendations
    - Travel tips

    Format using Markdown.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error generating itinerary: {str(e)}"


# ----------------------------
# Travel Assistant
# ----------------------------
def travel_chat(
    destination,
    itinerary,
    question
):
    if model is None:
        return "❌ Gemini API key not found. Check your .env file."

    prompt = f"""
    You are an expert travel assistant.

    Destination:
    {destination}

    Current Itinerary:
    {itinerary}

    User Question:
    {question}

    Give a helpful travel-related answer.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error generating response: {str(e)}"
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_itinerary(
    destination,
    budget,
    days,
    travelers,
    travel_style,
    interests
):

    prompt = f"""
    Create a detailed travel itinerary.

    Destination: {destination}
    Budget: ₹{budget}
    Days: {days}
    Travelers: {travelers}
    Travel Style: {travel_style}
    Interests: {', '.join(interests)}

    Include:
    - Day-wise itinerary
    - Recommended attractions
    - Food suggestions
    - Estimated costs
    - Travel tips

    Format in markdown.
    """

    response = model.generate_content(prompt)

    return response.text
# AGENTS.md

## Project Overview

AI Travel Planner is a Streamlit application powered by Gemini AI that generates travel itineraries and assists users with travel planning.

## AI Components

### 1. Itinerary Generator

* Uses Gemini API
* Generates day-wise travel plans
* Considers destination, budget, travel style, and interests

### 2. Budget Calculator

* Splits budget into:

  * Transport
  * Accommodation
  * Food
  * Activities

### 3. Travel Assistant

* Answers travel-related questions
* Uses itinerary context for personalized responses

### 4. PDF Generator

* Creates downloadable itinerary reports

### 5. Map Utility

* Displays destination location using map services

## Environment Variables

Required:

```
GEMINI_API_KEY
```

## Folder Structure

* `app.py` – Main application
* `pages/` – Streamlit pages
* `utils/` – Helper modules
* `assets/` – Images and styles
* `data/` – Static datasets
* `outputs/` – Generated files

## Future Enhancements

* Weather integration
* Hotel recommendations
* Flight booking APIs
* Expense analytics
* Multi-language support

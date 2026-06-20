# AI Travel Planner - User Manual

## Introduction

AI Travel Planner helps users generate personalized travel itineraries based on destination, budget, travel style, and interests using Gemini AI.

## Features

* AI-powered itinerary generation
* Budget allocation and tracking
* Travel assistant chatbot
* Interactive destination maps
* PDF itinerary export

## Getting Started

### Step 1

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 2

Create a `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
```

### Step 3

Run the application:

```bash
streamlit run app.py
```

## Using Trip Planner

1. Open Trip Planner.
2. Enter destination.
3. Enter budget.
4. Select travel style.
5. Choose interests.
6. Click "Generate Itinerary".

## Budget Tracker

View estimated allocations for:

* Transport
* Hotel
* Food
* Activities

## Travel Assistant

Ask travel-related questions about your destination or itinerary.

## Troubleshooting

### Gemini API Key Error

Verify that `.env` contains:

```
GEMINI_API_KEY=YOUR_API_KEY
```

### Quota Exceeded

Wait for the free-tier limit to reset or use another API key.

## Support

For issues, open a GitHub issue or contact the maintainers.

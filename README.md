# ✈️ AI Travel Planner

AI Travel Planner is a Streamlit-based web application that helps users plan trips effortlessly using Artificial Intelligence.

The application generates a complete travel itinerary based on the user's destination, budget, travel duration, number of travelers, and interests. It also provides budget allocation, weather information, travel recommendations, interactive maps, and downloadable PDF reports.

---

## 🚀 Features

### 🗺️ AI Itinerary Generation

Generate a detailed day-wise travel plan using AI.

### 💰 Smart Budget Planning

Automatically distribute the budget across:

* Transportation
* Accommodation
* Food
* Activities

### 🌤️ Weather Forecast

Get destination weather information to plan better.

### 📍 Interactive Maps

Visualize attractions and important locations on a map.

### 🤖 Travel Assistant

Ask travel-related questions through an AI-powered chatbot.

### 📄 PDF Export

Download the generated itinerary as a PDF report.

### 📊 Budget Tracker

Track expenses and monitor remaining budget during the trip.

---

## 📂 Project Structure

```text
ai-travel-planner/
│
├── app.py
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Trip_Planner.py
│   ├── 3_Budget_Tracker.py
│   └── 4_Travel_Assistant.py
│
├── utils/
│   ├── ai_generator.py
│   ├── budget_calculator.py
│   ├── weather.py
│   ├── pdf_generator.py
│   └── map_utils.py
│
├── data/
│   ├── destinations.csv
│   └── sample_itineraries.json
│
├── assets/
│   ├── logo.png
│   ├── banner.jpg
│   └── styles.css
│
├── outputs/
│   ├── generated_itinerary.pdf
│   └── trip_reports/
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Artificial Intelligence

* Google Gemini API

### Weather Data

* OpenWeather API

### Maps

* Folium
* Streamlit Folium

### PDF Generation

* ReportLab

### Data Storage

* CSV / JSON

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd ai-travel-planner
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 📖 Usage

1. Open the application.
2. Enter:

   * Destination
   * Budget
   * Number of Days
   * Number of Travelers
   * Interests
3. Click **Generate Trip**.
4. View:

   * Day-wise itinerary
   * Budget allocation
   * Weather information
   * Travel recommendations
5. Download the itinerary as a PDF.

---

## 📈 Future Enhancements

* Flight recommendations
* Hotel booking integration
* Real-time attraction suggestions
* Multi-language support
* Expense analytics dashboard
* Personalized travel recommendations

---

## 🎯 Hackathon Objective

Build an AI-powered travel planning assistant that creates personalized itineraries and helps travelers optimize their time, budget, and experience.

---

## 👥 Team

Developed as a Hackathon Project.

### Team Members

* Member 1
* Member 2

---

## 📄 License

This project is developed for educational and hackathon purposes.

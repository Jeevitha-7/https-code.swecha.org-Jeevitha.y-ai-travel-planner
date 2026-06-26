---
title: AI Travel Planner
emoji: ✈️
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.46.1"
python_version: "3.11"
app_file: app.py
pinned: false
---
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

## Quality, Security, and Testing Tools

* Semgrep security scanning is configured with `.semgrep.yml` and runs in CI.
* Biome is configured with `biome.json` and runs in CI for JavaScript/JSON checks.
* Test coverage reporting uses `pytest-cov` and publishes `coverage.xml` as a CI artifact.

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

## 🐳 Docker Deployment (Local test)

You can run the app inside Docker for a reproducible environment.

Build the image:

```bash
docker build -t ai-travel-planner:latest .
```

Run the container (uses `.env` for secrets):

```bash
docker run -d --name ai-travel-planner \
   --env-file .env -p 8501:8501 ai-travel-planner:latest
```

Check container logs to verify Streamlit started:

```bash
docker logs -f ai-travel-planner
```

Stop and remove the container when done:

```bash
docker stop ai-travel-planner && docker rm ai-travel-planner
```

Notes:
- Ensure your `.env` contains `GEMINI_API_KEY` and any other required keys.
- For production hosting, push the image to a container registry (Docker Hub, Render, etc.) and run on a host with proper secrets management.

---

## ☁️ Deployment Options (Render & Streamlit Cloud)

This project can be deployed either as a Docker-backed service (recommended for full control) or to Streamlit Community Cloud (simpler, but limited).

### A. Render (recommended for Docker)

1. Push your repository to GitHub.
2. Sign in to Render and create a new **Web Service**.
3. Connect your GitHub repository and select the branch to deploy.
4. Under **Environment**, choose **Docker** (Render will use the repository `Dockerfile`).
5. Set the following environment variables in Render's dashboard (Settings → Environment):

   - `GEMINI_API_KEY` — your Google Gemini API key
   - `OPENWEATHER_API_KEY` — (if used)

6. Leave the Docker build settings default (Render will build the image using the `Dockerfile`).
7. Deploy and monitor build logs in the Render dashboard.

Notes:
- If you need Ollama in production, self-host Ollama on a reachable host and update `utils/ai_generator.py` to point to that host. Ollama is not provided by Render by default.

### B. Streamlit Community Cloud (fast & simple)

1. Push the repository to GitHub.
2. Go to Streamlit Community Cloud and click **New app**.
3. Select your GitHub repo and branch; set `app.py` as the main file.
4. In the **Secrets** section, add:

   - `GEMINI_API_KEY` — your Google Gemini API key
   - `OPENWEATHER_API_KEY` — (if used)

5. Deploy — Streamlit Cloud will install dependencies from `requirements.txt` and run the app.

Limitations:
- Streamlit Cloud does not support running local services like Ollama; only remote APIs like Gemini will work.

### C. Post-deploy checklist

- Open the deployed URL and verify the UI loads.
- Generate a sample itinerary and confirm AI responses.
- Check logs for any `GEMINI_API_KEY` or network errors.

If you'd like, I can generate a ready-to-use Render `service.yaml` or a GitHub Actions workflow to build and push Docker images to a registry automatically.

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
## 🤖 Agent Development Kit (ADK) Integration

This project includes an AI Travel Agent built using an Agent-based architecture.

### Agent Features

* Travel itinerary generation
* Budget estimation
* Destination recommendations
* Travel assistance through natural language interaction
* Memory-ready architecture for user preferences
* Tool orchestration support

### Agent Workflow

User Query
→ Travel Agent
→ Reasoning Process
→ Travel Planning Tools
→ Response Generation

### Agent Demo

Users can interact with the AI Travel Agent directly from the application home page by entering travel-related queries.

Example:

Input:
Plan a 3-day trip to Goa for 2 people under ₹15,000

Output:
A personalized itinerary with budget recommendations and travel suggestions.

---

## 🔑 BYOK (Bring Your Own Key)

The application supports BYOK for Gemini API access.

Users can provide their own Gemini API key directly within the application to access AI-powered features.

Required Key:

* Google Gemini API Key

Benefits:

* No shared API dependency
* Better privacy
* User-controlled AI access
* Easy deployment on different environments

---

## 🧠 Local AI Support (Optional)

The project architecture is designed to support local AI inference using tools such as:

* Ollama
* Local LLMs
* Gemini API

This allows future deployment without relying entirely on external AI services.
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

* Jeevitha.Y
* Dhruva.G

---

## 📄 License

This project is developed for educational and hackathon purposes.

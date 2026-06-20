from utils.ai_generator import generate_plan, generate_itinerary, travel_chat


def test_generate_plan_basic():
    result = generate_plan("Goa", 3)
    assert isinstance(result, dict)
    assert result["destination"] == "Goa"
    assert result["days"] == 3
    assert "plan" in result


def test_generate_plan_edge():
    result = generate_plan("", 0)
    assert isinstance(result, dict)
    assert result["days"] == 0


def test_generate_plan_types():
    result = generate_plan("Paris", 5)
    assert isinstance(result["plan"], list)


def test_generate_itinerary_fallback():
    result = generate_itinerary("Goa", 10000, 3, 2, "budget", ["beach"])
    assert isinstance(result, str)


def test_travel_chat_fallback():
    result = travel_chat("Goa", "Day 1 plan", "What should I eat?")
    assert isinstance(result, str)


def test_itinerary_no_api(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    result = generate_itinerary("Goa", 1000, 3, 2, "budget", ["food"])
    assert "Error" in result or "API key" in result

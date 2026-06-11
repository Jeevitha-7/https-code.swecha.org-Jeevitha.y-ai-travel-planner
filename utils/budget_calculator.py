def calculate_budget(total_budget):
    return {
        "transport": int(total_budget * 0.40),
        "hotel": int(total_budget * 0.30),
        "food": int(total_budget * 0.15),
        "activities": int(total_budget * 0.15),
    }

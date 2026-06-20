# utils/budget_calculator.py


def calculate_budget(total_budget, days):
    """
    Safely calculate per-day budget.
    """
    if days <= 0:
        return 0

    return total_budget / days

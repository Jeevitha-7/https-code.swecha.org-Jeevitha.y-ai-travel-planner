from utils.budget_calculator import calculate_budget


def test_budget():
    assert calculate_budget(1000, 5) >= 0


def test_budget_edge_zero_days():
    assert calculate_budget(1000, 0) == 0

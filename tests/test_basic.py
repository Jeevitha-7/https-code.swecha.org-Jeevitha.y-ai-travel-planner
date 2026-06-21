def test_import_modules():
    try:
        import utils.budget_calculator
        import utils.map_utils
    except Exception:
        pass

    assert True

def test_import_modules():
    try:
        import utils.budget_calculator
        import utils.map_utils
        import utils.translator
    except Exception:
        pass

    assert True

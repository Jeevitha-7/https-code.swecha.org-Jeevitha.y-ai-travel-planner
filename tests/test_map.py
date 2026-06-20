from utils.map_utils import get_map


def test_map():
    assert get_map("India") is not None


def test_map_empty_string():
    result = get_map("")
    assert result is not None

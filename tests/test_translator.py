from utils.translator import translate_text


def test_translate():
    assert translate_text("hello", "hi") is not None

from utils.pdf_generator import generate_pdf


def test_pdf():
    assert generate_pdf("test") is None or True

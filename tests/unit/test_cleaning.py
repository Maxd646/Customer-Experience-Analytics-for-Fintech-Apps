from src.fintech_app_reviews.preprocessing.cleaning import clean_text

def test_clean_text():
    assert clean_text("Hello!!!") == "hello"
    assert clean_text("App   is Good") == "app is good"

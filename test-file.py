import pytest
from app import translate

def test_translation_to_french():
    print("Starting French translation test")
    result = translate("Hello", "French")
    print(f"French translation result: {result}")
    assert result.lower() in ["bonjour", "salut"], f"Expected 'Bonjour' or 'Salut', but got {result}"

def test_translation_to_german():
    print("Starting German translation test")
    result = translate("Hello", "German")
    print(f"German translation result: {result}")
    assert result.lower() == "hallo", f"Expected 'Hallo', but got {result}"

def test_translation_to_romanian():
    print("Starting Romanian translation test")
    result = translate("Hello", "Romanian")
    print(f"Romanian translation result: {result}")
    assert result.lower() == "salut", f"Expected 'Salut', but got {result}"

def test_unsupported_language():
    print("Starting unsupported language test")
    result = translate("Hello", "Spanish")
    print(f"Unsupported language result: {result}")
    assert result == "Sorry, this language is not supported."

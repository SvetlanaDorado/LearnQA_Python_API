def test_phrase_length():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, f"Phrase length is {len(phrase)} characters, but it should be less than 15"
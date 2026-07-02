from toolkit.text import word_count


def test_word_count():
    assert word_count("Hello AI") == 2


def test_empty_text():
    assert word_count("") == 0


def test_spaces():
    assert word_count("     ") == 0
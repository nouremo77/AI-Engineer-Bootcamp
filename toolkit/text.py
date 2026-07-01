import string

def clean_text(text: str) -> str:
    """
    Clean and normalize text.

    Args:
        text: Input text.

    Returns:
        Cleaned text.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, got {type(text).__name__}")
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.split())
    return text

#________________________________________________________________________________

def word_count(text: str) -> int:
    """
    Count the number of words in the text.

    Args:
        text: Input text.

    Returns:
        Number of words.
    """
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    return len(words)

#_____________________________________________________________________________________

def char_count(text: str) -> int:
    """
    Count the number of characters in the text.

    Args:
        text: Input text.

    Returns:
        Number of characters.
    """
    cleaned_text = clean_text(text)
    cleaned_text.replace(" ", "")
    return len(cleaned_text.replace(" ", ""))
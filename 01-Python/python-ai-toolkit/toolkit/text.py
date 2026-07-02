import string
from collections import Counter

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

#_____________________________________________________________________________________

import re

def sentence_count(text: str) -> int:
    """
    Count the number of sentences in the text.

    Args:
        text: Input text.

    Returns:
        Number of sentences.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, got {type(text).__name__}")

    text = text.strip()

    if not text:
        return 0

    # Find groups of sentence-ending punctuation
    sentences = re.findall(r"[.!?]+", text)

    if sentences:
        return len(sentences)

    # Text without punctuation is considered one sentence
    return 1

#_____________________________________________________________________________________

def unique_words(text: str) -> int:
    """
    Get the set of unique words in the text.

    Args:
        text: Input text.

    Returns:
        Set of unique words.
    """
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    unique= set(words)
    return len(unique)

#_____________________________________________________________________________________

def most_common_word(text: str) -> str:
    """
    Return the most common word in the text.

    Args:
        text: Input text.

    Returns:
        The most common word.
        Returns an empty string if the text is empty.
    """
    cleaned_text = clean_text(text)

    if not cleaned_text:
        return ""

    words = cleaned_text.split()

    word_counts = Counter(words)

    return word_counts.most_common(1)[0][0]
from toolkit.text import clean_text, word_count, char_count, sentence_count, unique_words
print(clean_text("Hello,,, AI!!!"))
print(clean_text("   Python     Engineer   "))
print(clean_text("Hello\nWorld"))

print(word_count("Hello AI Engineer"))
print(word_count(""))
print(word_count("     "))
print(word_count("Hello\nWorld"))


print(char_count("Hello AI Engineer"))
print(char_count(""))
print(char_count("     "))
print(char_count("Hello\nWorld"))

print(sentence_count("Hello AI Engineer! How are you?"))
print(sentence_count(""))
print(sentence_count("     "))
print(sentence_count("Hello\nWorld"))

print(unique_words("Hello AI Engineer Hello"))
print(unique_words(""))
print(unique_words("     "))
print(unique_words("Hello\nWorld"))
'''
print(most_common_words("Hello AI Engineer Hello"))
print(most_common_words(""))
print(most_common_words("     "))
print(most_common_words("Hello\nWorld"))'''
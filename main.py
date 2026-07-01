from toolkit.text import clean_text, word_count, char_count

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
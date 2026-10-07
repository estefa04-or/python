text = "A man, a plan, a canal: Panama"

def count_words(text):
    counts = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def is_palindrome(text):
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned += char
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text

print(count_words(text))
print(is_palindrome(text))
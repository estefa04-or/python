import time

# ---- Timer Decorator ----
def timer(func):
    def wrapper(*args, **kwargs):      # edit 1: accept any arguments
        start = time.time()
        result = func(*args, **kwargs)  # edit 2: pass them on and save the answer
        end = time.time()
        print(f"Function took {end - start} seconds to execute.")
        return result                   # edit 3: give the answer back
    return wrapper

@timer
def slow():
    total = 0
    for i in range(1000000):
        total += i

slow()


@timer
def sum_list():
    return sum([x for x in range(1, 1000001)])

@timer
def sum_generator():
    return sum(x for x in range(1, 1000001))

print(sum_list())
print(sum_generator())



# ---- Count Words ----
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

# ---- Palindrome Checker ----
def is_palindrome(text):
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned += char
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text

print(count_words(text))
print(is_palindrome(text))


# ---- Shout Decorator ----
def shout(func):
    def wrapper():
        print("Starting")
        func()
        print("Done")
    return wrapper

@shout
def say_hi():
    print("Hi!")
say_hi()
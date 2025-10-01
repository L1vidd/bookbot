def get_num_words(book_text):
    total_words = book_text.split()
    num_words = len(total_words)
    return num_words

def get_num_chars(book_text):
    num_chars = {}
    book_text = book_text.lower()
    for char in book_text:
        if char not in num_chars:
            num_chars[char] = 1
        else: 
            num_chars[char] += 1
    return num_chars

def sort_on(item):
    return item["num"]

def sort_chars(num_chars):
    sorted_chars = []
    for char in num_chars:
        if char.isalpha() is True:
            sorted_chars.append({"char": char, "num": num_chars[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
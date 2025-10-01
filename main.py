def get_book_text(path_to_text):
    with open(path_to_text) as f:
        return f.read()

from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars

def main():
    book = "./books/frankenstein.txt"
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_chars = sort_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["char"]}:", char["num"])
    print("============= END ===============")
main()
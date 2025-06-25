from stats import get_num_words, get_chars_dict


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} totals words")
    print("--------- Character Count -------")
    # sorted list of dictionaries here
    print("============= END ===============")


def get_book_text(path):
    with open(path) as file:
        return file.read()

# def sort_on()

main()

from stats import get_num_words, get_chars_dict, get_chars_list


def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_chars_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} totals words")
    print("--------- Character Count -------")
    print_report(chars_list)
    print("============= END ===============")


def get_book_text(path):
    with open(path) as file:
        return file.read()
    

def sort_on(unsorted_list):
    return unsorted_list["num"]


def print_report(chars_list):
    for i in range(0, len(chars_list)):
        char_key = chars_list[i]['char']
        if char_key.isalpha() == True:
            print(f"{char_key}: {chars_list[i]['num']}")


main()

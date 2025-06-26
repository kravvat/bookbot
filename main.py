import sys # import sys module so we can get rid of a hardcoded book_path
from stats import ( # import functions defined in other file
    get_num_words, 
    get_chars_dict, 
    chars_dict_to_sorted_list,
)


def main(): # this will be executed on 'python3 main.py'
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] # path to file that we want to analyze

    text = get_book_text(book_path) # file as a string
    num_words = get_num_words(text) # word count
    chars_dict = get_chars_dict(text) # dictionary with chars as keys and their count as values
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict) # list that separates each char/count pair into individual dictionary
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path): # converts our file to string
    with open(path) as file:
        return file.read()
    

def print_report(book_path, num_words, chars_sorted_list): # shows main report while ignoring non-alphabetical chars
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...") # show which file is being analyzed
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words") # print total number of words
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")


main()

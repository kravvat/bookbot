from stats import get_num_words, get_chars_dict, get_chars_list # import functions defined in other file


def main(): # this will be executed on 'python3 main.py'
    book_path = "books/frankenstein.txt" # path to file that we want to analyze
    text = get_book_text(book_path) # file as a string
    num_words = get_num_words(text) # word count
    chars_dict = get_chars_dict(text) # dictionary with chars as keys and their count as values
    chars_list = get_chars_list(chars_dict) # list that separates each char/count pair into individual dictionary
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...") # show which file is being analyzed
    print("----------- Word Count ----------")
    print(f"Found {num_words} totals words") # print total number of words
    print("--------- Character Count -------")
    print_report(chars_list) # print main report
    print("============= END ===============")


def get_book_text(path): # converts our file to string
    with open(path) as file:
        return file.read()
    

def sort_on(unsorted_list): # tells .sort() method that it should use value of a "num" key as a key
    return unsorted_list["num"]


def print_report(chars_list): # shows main report while ignoring non-alphabetical chars
    for i in range(0, len(chars_list)):
        char_key = chars_list[i]['char']
        if char_key.isalpha() == True:
            print(f"{char_key}: {chars_list[i]['num']}")


main()

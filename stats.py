def get_num_words(text): # calculates the word count
    words = text.split()
    return len(words)


def get_chars_dict(text): # dictionary with chars as keys and their count as values
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict): # this tells .sort() that it should use values from "num" key as a reference
    return dict["num"]


def sort_on(unsorted_list): # tells .sort() method that it should use value of a "num" key as a key
    return unsorted_list["num"]


def chars_dict_to_sorted_list(num_chars_dict): # packs char/count pairs into separate dictionaries and puts these dictionaries into a sorted list
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

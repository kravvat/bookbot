def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(items):
    return items["num"]


def get_chars_list(chars_dict):
    chars_list = []
    for char in chars_dict:
        char_count = chars_dict[char] 
        chars_list.append({'char': char, 'num': char_count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

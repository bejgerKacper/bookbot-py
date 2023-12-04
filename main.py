def main():
    file_path = "books/frankenstein.txt"
    txt_file = open_txt_file(file_path)
    words_count = get_words_count(txt_file)
    chars_dict = get_chars_dict(txt_file)
    chars_list = get_list_alpha_chars(chars_dict)
    print_report(file_path, words_count, chars_list, chars_dict)

def open_txt_file(file_path):
    return open(file_path).read()

def get_words_count(txt_file):
    return len(txt_file.split())

def get_lower_chars(txt_file):
    return txt_file.lower()

def print_report(words, char_dictionary, book_path):
    print(f"--- Begin raport of book {book_path} ---")
    print(f"{words} words found in the document")
    chars = dictionary_to_list(char_dictionary)
    chars.sort()
    for char in chars:
        print(f"The {char} character was found {char_dictionary[char]} times")
    print("--- End raport ---")

def dictionary_to_list(char_dictionary):
    char_list = []
    for char in char_dictionary:
        if char.isalpha():
            char_list.append(char)
    return char_list

def count_letters(text_file):
    char_dictionary = {}
    for letter in text_file:
        lowered = letter.lower()
        if lowered in char_dictionary:
            char_dictionary[lowered] += 1
        else:
            char_dictionary[lowered] = 1
    return char_dictionary

main()
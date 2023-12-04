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

def open_file(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(string_file): 
    return len(string_file.split())

def main():
    book_path = "books/frankenstein.txt"
    text_file = open_file(book_path)
    words_counted = count_words(text_file)
    char_dictionary = count_letters(text_file)
    print_report(words_counted, char_dictionary, book_path)

main()
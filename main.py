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

#total count of every single character in txt_file as [char]:count
def get_chars_dict(txt_file):
    lower_chars = get_lower_chars(txt_file)
    chars_dict = {}
    for char in lower_chars:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

#list of all alphabetical character in chars_dict
def get_list_alpha_chars(chars_dict):
    chars_list = []
    for char in chars_dict:
        if char.isalpha():
            chars_list.append(char)
    chars_list.sort()
    return chars_list

def print_report(words, char_dictionary, book_path):
    print(f"--- Begin raport of book {book_path} ---")
    print(f"{words} words found in the document")
    chars = dictionary_to_list(char_dictionary)
    chars.sort()
    for char in chars:
        print(f"The {char} character was found {char_dictionary[char]} times")
    print("--- End raport ---")

main()
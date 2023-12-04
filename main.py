def count_letters(string_file):
    letter_dictionary = {}
    for letter in string_file:
        lowered = letter.lower()
        if lowered in letter_dictionary:
            letter_dictionary[lowered] += 1
        else:
            letter_dictionary[lowered] = 1
    print(letter_dictionary)

def open_file(file_path):
    with open(file_path) as f:
        return f.read()

def split_text(string_file): 
    return len(text_file.split())

def main():
    string_file = open_file("/Users/kacper-bejger/workspace/github.com/bejgerKacper/bookbot-py/books/frankenstein.txt")
    # words = split_text(text_file)
    # print(words)
    count_letters(string_file)

main()
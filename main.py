def count_letters(strings):
    letter_dictionary = {}
    for letter in strings:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
    print(letter_dictionary)

def open_file(file_path):
    with open(file_path) as f:
        text_file = f.read()
    return text_file

def split_text(text_file): 
    words = text_file.split()
    return len(words)

def main():
    text_file = open_file("/Users/kacper-bejger/workspace/github.com/bejgerKacper/bookbot-py/books/frankenstein.txt")
    # words = split_text(text_file)
    # print(words)
    count_letters(text_file)

main()
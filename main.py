def count_letters(text_file):

def open_file(file_path):
    with open(file_path) as f:
        text_file = f.read()
    return text_file

def split_text(text_file):
    words = text_file.split()
    return len(words)

def main():
    text_file = open_file("/Users/kacper-bejger/workspace/github.com/bejgerKacper/bookbot-py/books/frankenstein.txt")
    words = split_text(text_file)
    print(words)

main()
from collections import defaultdict


# grabs text file from filepath and returns contents as a single string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


# Gets the word count from the provided .txt file
def get_num_words(filepath):
    file_contents = get_book_text(filepath)
    word_count = len(file_contents.split())
    return word_count


# Creates a dictionary for every character in the .txt file provided and counts each instance of that character
def count_all_chars(filepath):
    file_contents = get_book_text(filepath)
    char_count = defaultdict(int)
    for char in file_contents:
        char_count[char.lower()] += 1
    return char_count


# Takes the dictionary of character counts and retruns it as a list of dict's and then sorts it
def list_of_counted_chars(filepath):
    char_count = count_all_chars(filepath)
    char_list = []
    for key, val in char_count.items():
        tmp_dict = {"name": key, "num": val}
        char_list.append(tmp_dict)

    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list

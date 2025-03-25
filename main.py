from stats import *  # noqa: F403
import time
# Open a text file and print the contents out to the console


def main():
    selected_filepath = "Books/frankenstein.txt"
    print_report(selected_filepath)


def print_report(filepath):
    word_count = get_num_words(filepath)
    char_count = list_of_counted_chars(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    time.sleep(3)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in char_count:
        if i["name"].isalpha():
            name = i["name"]
            num = i["num"]
            print(f"{name}: {num}")
    print("============= END ===============")


main()

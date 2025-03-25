from stats import *  # noqa: F403
import sys
# Open a text file and print the contents out to the console


def main():
    if len(sys.argv) == 2:
        try:
            selected_filepath = sys.argv[1]
            print_report(selected_filepath)
        except FileNotFoundError:
            print("Filepath given is invalid. Please try again")
            sys.exit(1)
    else:
        print("Please provide a filepath. Example: python3 main.py <path_to_book>")
        sys.exit(1)


def print_report(filepath):
    word_count = get_num_words(filepath)
    char_count = list_of_counted_chars(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
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

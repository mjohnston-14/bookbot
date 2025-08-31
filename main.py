import sys

def get_book_text(filename):
    file_contents = ""
    with open(filename) as f:
        file_contents = f.read()
    return file_contents
def get_num_words(file):
    return file.split()

from stats import get_num_words, get_char_count

def main():
    filename = ""
    args = len(sys.argv)
    if args < 2 or args > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filename = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    words_counted = len(get_num_words(get_book_text(filename))) 
    print("----------- Word Count ----------")
    print(f"Found {words_counted} total words")

    char_count = get_char_count(get_book_text(filename))
#    char_count.sort()

    print("--------- Character Count -------")
    for c in char_count:
        print(f"{c.get("name")}: {c.get("num")}")
#    print(f"{char_count}")
    sys.exit(0)

main()

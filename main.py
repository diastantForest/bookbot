book_path = "books/frankenstein.txt"


def main():
    text = get_book_text(book_path)
    num_words = get_num_worgs(text)
    stats_dictionary = get_char_stat(text)
    stats_list = list(stats_dictionary.items())
    stats_list.sort()

    # print a report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char_tul in stats_list:
        if char_tul[0].isalpha():
            print(f"The '{char_tul[0]}' character was found {char_tul[1]} times")

    print("--- End Report ---")
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_worgs(string):
    words = string.split()
    return len(words)

def get_char_stat(string):
    stats = dict()
    for char in string:
        try:
            stats[char.lower()] += 1
        except KeyError as ke:
            stats[char.lower()] = 1
    return stats

main()

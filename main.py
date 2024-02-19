def main():
    book_name = "frankenstein"
    book_name = capitalize_first_letter(book_name)
    book_string = read_book(book_name)
    word_count = count_words(book_string)
    character_count_dictionary = create_character_count_dictionary(book_string)
    count_letter_dictionary_list = create_sorted_dictionary_list(character_count_dictionary)
    print_report(book_name, word_count, count_letter_dictionary_list)
    

def print_report(book_name, word_count, count_letter_dictionary_list):
    relPath = f"books/{book_name.lower()}.txt"
    print(f"--- Begin report of {relPath} ---")
    print(f"{word_count} words found in the document \n")
    for sub_dict in count_letter_dictionary_list:
        print(f"The letter \'{sub_dict["letter"]}\' was found {sub_dict["count"]} times")
    print("--- End report ---")


def read_book(book_name):
    relPath = f"books/{book_name.lower()}.txt"
    with open(relPath) as book:
        book_string = book.read()
    return book_string


def count_words(book_string):
    book_array = book_string.split()
    word_count = len(book_array)
    return word_count
    
    
def capitalize_first_letter(word):
    capitalized_word = word[0].upper() + word[1:]
    return capitalized_word
    

def create_character_count_dictionary(book_string):
    character_count_dictionary = {}
    for character in book_string:
        character = character.lower()
        if character in character_count_dictionary.keys():
            character_count_dictionary[character] += 1
        else:
            character_count_dictionary[character] = 1
    return character_count_dictionary


def sort_on(dict):
    return dict["count"]


def create_sorted_dictionary_list(character_dictionary):
    count_letter_dictionary_list = []
    for key in character_dictionary:
        if key.isalpha():
            count_letter_dictionary_list.append({"letter": key, "count": character_dictionary[key]})
    count_letter_dictionary_list.sort(reverse=True, key=sort_on)
    return count_letter_dictionary_list
    

main()
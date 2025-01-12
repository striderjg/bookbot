#!/usr/bin/env python3

# ============= Functions =======================
def get_word_count(s):
    return len(s.split())

def get_char_count(s):
    char_count = {}
    lstr = s.casefold()
    for char in range(0x61, 0x7B):
        char_count[chr(char)] = lstr.count( chr(char) )
    return char_count


# ============ Program Entry Point ====================
def main():
    book_title = "books/frankenstein.txt"
    with open(book_title) as f:
        file_contents = f.read()
        
    print(f"--- Begin Report on {book_title} ---")
    print( f"{get_word_count(file_contents)} words found in {book_title}" )

    char_count_dict = get_char_count(file_contents)
    for char in char_count_dict: 
        print( f"The '{char}' character was found {char_count_dict[char]} times" )
    print("--- End Report ---")
    #print(get_char_count(file_contents))

main()
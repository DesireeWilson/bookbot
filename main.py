import sys
from stats import get_num_words
from stats import count_characters

def get_book_text(filePath): 
    with open(filePath) as f:
        file_contents = f.read()
        return file_contents
def sort_dictionary(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    
def print_output(filePath, num_words, char_dict_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for (key, value) in char_dict_sorted.items():
        print(f"{key}: {value}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("To use this program, please refer to the following example: python3 main.py <path_to_book>")
        sys.exit(1)        
    filePath = sys.argv[1]
    contents = get_book_text(filePath)
    num_words = get_num_words(contents)
    #output = f"{num_words} words found in the document"
    #print(output)
    d = count_characters(contents)
    #print(d)
    d_sorted = sort_dictionary(d)
    print_output(filePath, num_words, d_sorted)

if __name__ == "__main__":
    main()
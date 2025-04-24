def get_num_words(text):
    num_words = 0
    lines = text.split("\n")
    for line in lines:
        words = line.split(" ")
        for word in words:
            if word != "":
                num_words += 1
    return num_words

def count_characters(text):
    char_d = {}
    lines = text.lower().split("\n")
    for line in lines:
        words = line.split(" ")
        for word in words:
            if word != "":
                for letter in word:
                    #if letter is in dictionary, update the count
                    if(letter in char_d.keys()):
                        count = char_d.get(letter) + 1
                        char_d.update({letter: count})
                    #else, add the letter and count = 1 to dictionary
                    else:
                        char_d.update({letter: 1})
    return char_d
            
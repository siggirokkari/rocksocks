def create_word_list(filepath):
    file = open(filepath,"r")
    hangman_words_list = file.readlines()
    word_list = []
    for i in range(len(hangman_words_list)):
        word_list.append(hangman_words_list[i].rstrip("\n"))
    file.close()
    return word_list

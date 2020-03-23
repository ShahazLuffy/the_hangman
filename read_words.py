def read_secret():
    my_text = open("words.txt", "r")
    my_list = my_text.read().split("\n")
    my_text.close()
    return my_list


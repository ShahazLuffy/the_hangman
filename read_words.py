def read_secret():
    my_text = open("words.txt", "r")
    my_list = my_text.read().split(",")
    return my_list
    my_text.close()


import read_words
import random

u = random.randint(0, len(read_words.read_secret()) - 1)
secret = read_words.read_secret()[u]
right_guess = []
secret_list = []

for x in range(0, len(secret)):
    secret_list.append("_")
n = 10
flag = True
while flag:
    guessed_word = input(print("guess the word !"))
    if len(guessed_word) > 1:
        print("your guess must be only 1 character at a time")
        continue
    n -= 1
    print(n)

    for i in range(0, len(secret)):
        if secret[i] == guessed_word.lower():
            secret_list[i] = guessed_word
            right_guess.append(guessed_word)

    print(secret_list)

    if n < 0:
        flag = False
        break
    if len(secret) == len(right_guess):
        flag = True
        break

if not flag:
    print("you lose")
else:
    print("you win")

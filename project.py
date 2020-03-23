import read_words
import random

u = random.randint(0, len(read_words.read_secret()) - 1)
secret = read_words.read_secret()[u]
chances = []
for x in range(0, len(secret)):
    chances.append("*")
right_guess = []
secret_list = []
characer_entered = []

for x in range(0, len(secret)):
    secret_list.append("_")
print(secret_list)
print (chances)
n = len(secret)
flag = True
while flag:
    guessed_word = input("guess the word !\n")
    if guessed_word not in characer_entered:
        if len(guessed_word) > 1:
            print("your guess must be only 1 character at a time")
            continue

        characer_entered.append(guessed_word)

        found = False
        for i in range(0, len(secret)):
            if secret[i] == guessed_word.lower():
                found = True
                secret_list[i] = guessed_word
                right_guess.append(guessed_word)

        if not found:
            chances[len(secret) - n] = guessed_word
            n -= 1

        print(secret_list)
        print(chances)

        if n <= 0:
            flag = False
            break
        if len(secret) == len(right_guess):
            flag = True
            break
    else:
        print("you already guessed this word, try again")

if not flag:
    print("you lose, the word was ", secret)
else:
    print("you win, the word was ", secret)

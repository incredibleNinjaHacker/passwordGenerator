import random
import string
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'derpy', 'dumb']
nouns = ['derp', 'camel', 'apple', 'dinosaur', 'goat', 'toaster', 'dragon', 'mario', 'videogame', 'duck', 'panda', 'duck', 'chicken']
print("welcome to dat ultimate password picker!!!!")
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print("your new password is: %s" % password)
    responce = input("would you like another password?Type y or n")
    if responce == "n":
        break

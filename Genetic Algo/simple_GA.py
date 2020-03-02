import random

target = 'Umai owa mou sindore. Nani?'
charecters = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!'

def makelist():
    charlist = []
    for i in range(len(target)):
        charlist.append(random.choice(charecters))

    return charlist

def score(mylist):
    #score by comparing generated list to target list 
    matches = 0
    for i in range(len(mylist)):
        if mylist[i] == target[i]:
            matches += 1
    return matches

def mutate(mylist):
    # randomly changes one charecter
    new_list = list(mylist)
    new_letter = random.choice(charecters)
    index = random.randint(0, len(target) - 1)
    new_list[index] = new_letter
    return new_list

best_list = makelist()
best_score = score(best_list)
guesses = 0

# Main loop

while True:
    guess = mutate(best_list)
    guess_score = score(guess)
    guesses += 1

    if guess_score <= best_score:
        continue

    print('Guess: ', guesses)
    print(''.join(guess))
    print('Score: ', guess_score)
    print('------------------------')

    if guess_score == len(target):
        break

    best_list = list(guess)
    best_score = guess_score

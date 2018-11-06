#console-based game
import random

animalanswer = [
    'CHICKEN', 'DUCK', 'WHALE', 'DOG', 'CAT', 'GOOSE', 'MOUSE', 'SHARK'
    'CROCODILE', 'PARROT', 'TIGER', 'LION', 'GIRAFFE', 'SNAKE', 'ELEPHANT',
    'MONKEY', 'ORANG UTAN', 'WORM', 'ANT', 'FLEA', 'BEAR', 'DEER', 'PANDA'
    ]

#correct answer
correct_answer = random.choice(animalanswer)
correct_blank_answer = []
correct_answer_in_alphabet = []

#player answer
player_guess = ''
player_lifes = 6
player_already_guessed = []

#convert correct answer to blank
for alphabet in correct_answer:
    correct_answer_in_alphabet.append(alphabet)
    if alphabet == ' ':
        correct_blank_answer.append(' ')
    else:
        correct_blank_answer.append('_ ')

while player_lifes > 0:

    #print('(Cheat) Answer: ')
    #print(''.join(correct_answer_in_alphabet))
    print('*Reminder* If you guessed more than 1 letter, only the first letter would be checked.')
    print('*TURN CAPSLOCK ON! IF NOT YOUR ANSWER CONSIDERED AS WRONG!*')
    print('Guess: ' + ' '.join(correct_blank_answer) + ' ')
    print('Lifes: ', player_lifes)
    print('What you guessed already: ')
    if len(player_already_guessed) == 0:
        print('None')
    else:
        print(' '.join(player_already_guessed))

    player_guess = input('Guess 1 letter: ')[:1]
    if player_guess not in player_already_guessed:
        # check
        for character in range(0, len(correct_answer_in_alphabet)):
            if player_guess == correct_answer_in_alphabet[character]:
                correct_blank_answer[character] = correct_answer_in_alphabet[character]

        player_already_guessed.append(player_guess)

        if player_guess not in correct_answer_in_alphabet:
            player_lifes = player_lifes - 1

        if correct_blank_answer == correct_answer_in_alphabet:
            break;

    else:
        print('You already guessed {}!'.format(player_guess))

if player_lifes == 0:
    print('You Lose! Player have {} life(s) left.'.format(player_lifes))
    print('The correct answer is ', correct_answer)
else:
    print('Player guessed {} correctly!'.format(correct_answer))
    print('You Win! Player have {} life(s) left.'.format(player_lifes))
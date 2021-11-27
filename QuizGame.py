def new_game():

    guesses = []
    correct_guess = 0
    que_num = 1

    for key in que:
        print('---------------')
        print(key)
        for i in ans[que_num-1]:
            print(i)

        guess = input("Enter A , B , C , D  : ").upper()
        guess = guess.upper()
        guesses.append(guess)


        correct_guess += check_answer(que.get(key), guess)

        que_num += 1


        display_score(correct_guess, guesses)




def check_answer(ans, guess):
    if ans == guess:
        print('Correct')
        return 1
    else:
        print('Wrong')
        return 0
def display_score(correct_guess, guesses):
    print('-------------------')
    print('Results')
    print('-------------------')

    print('Answers: ', end = "")
    for  i in que:
        print(que.get(i), end="")
    print()

    print('Guesses: ', end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guess/ len(que))*100)
    print('Your score is: '+ str(score)+ '%')


def play_again():
    responce = input("Play Again?: (Yes/No)")
    responce = responce.upper()
    if responce == 'Yes':
        return True
    else:
        return False


que = {
    'Who is the current president of Russia?: ':'A',
    'Is Russia a continent?: ':'B',
    'Where does Putin live?: ':'C',
    "Putin's Birthdays is: ":'D'
}

ans = [["A. Vladimir Putin", "B. Boris Yeltsin", "C. Dmitry Medvedev", "D. Viktor Chernomyrdin"],
       ["A. Africa", "B. Eurasia", "C. America", "D. Asia"],
       ["A. White House", "B. Pentagon", "C. Kremlin", "D. Mausoleum"],
       ["A. 19.08.1952", "B. 22.07.1952", "C. 12.09.1952", "D. 07.10.1952"]]

new_game()
while play_again():
    new_game()

print('Byeee')

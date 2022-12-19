from random import choice


while True:    
    series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

    win = []

    while len(win) < 4:
        draw = choice(series)
        if draw not in win:
            win.append(str(draw))
    
    print("\nWelcome to the lottery! Enter 'q' at any time to quit.")
    pick = input("Pick any number from '1 - 10', or a letter from 'a - e': ")

    if pick == 'q':
        break
    elif pick in win:
        print("\nCongratulations! That was a winning pick! Winner winner chicken dinner!")
        print("These were all the winning draws:")
        for char in win:
            print(str(char))
        print("Let's play again!")
    else:
        print("\nSorry, you lose!")
        print("These were all the winning draws:")
        for char in win:
            print(str(char))
        print("Let's play again!")
        



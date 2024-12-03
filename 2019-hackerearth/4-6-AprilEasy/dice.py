"""
There are number of girls and they rolled a dice in turns one after another.
If the number on the dice is 6, then the dice will be rolled again until she get a number other than 6.
Since you know the sequence of numbers which the dice shows when rolled each time, you have to find what is the total number of girls or if the sequence is invalid.
"""

dice_throws = list(input())

if len(dice_throws) > 100000:
    print(-1)
else:
    girls = 0
    illegale = False
    for throw in dice_throws:
        if 6 > int(throw) > 0:
            girls = girls + 1
        elif int(throw) != 6:
            illegale = True

    if illegale == True:
        print(-1)
    elif len(dice_throws) > 0 and girls == 0:
        print(-1)
    elif len(dice_throws) == 0:
        print(-1)
    elif dice_throws[len(dice_throws) - 1] == str(6):
        print(-1)
    else:
        print(girls)

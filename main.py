import random


def roll():
    return random.randint(1, 6)


def twentyorGoal2(score):
    total = 0
    done = False
    while total < 20 and not done and total + score < 100:
        result = roll()
        print("Roll:", result)
        if result == 1:
            total = 0
            done = True
        else:
            total += result
    print("Turn Total:", total)
    return total


def rollAgian(string):
    Answer = input(string)
    if Answer != "" and (Answer[0].lower() == "y"):
        return True
    elif Answer != "" and (Answer[0].lower() == "n"):
        return False
    else:
        return rollAgian(string)


def twentyorGoal(score):
    total = 0
    done = False
    while total < 20 and not done and total + score < 100:
        result = roll()
        print("Roll:", result)
        rollagian = rollAgian("Do you want to roll agian?")
        if result == 1:
            total = 0
            done = True
        else:
            total += result
        if rollagian:
            pass
        elif rollagian == True and result == 1:
            done = True
        else:
            done = True
    print("Turn Total:", total)
    return total


def gameover(player1Score, player2Score):
    if (player1Score >= 100 or player2Score >= 100) and player1Score != player2Score:
        return True
    else:
        return False


def twoplayer():
    player1Score = 0
    player2Score = 0

    while True:
        print("Player 1 score: ", str(player1Score))
        print("Player 2 score: ", str(player2Score))
        print("its player 1's turn")
        player1Score += twentyorGoal2(player1Score)
        print("Player 1 new score: ", str(player1Score))
        player2Score += twentyorGoal(player2Score)
        print("Player 2 new score: ", str(player2Score))
        print("Player 1 score: ", str(player1Score))
        print("Player 2 score: ", str(player2Score))
        if gameover(player1Score, player2Score):
            break


print(twoplayer())


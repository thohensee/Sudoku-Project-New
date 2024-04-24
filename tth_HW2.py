
# Homework 2 - Blackjack Simulator

from p1_random import P1Random

rng = P1Random()

gameContinue = True
gameNum = 0
playerWins = 0
dealerWins = 0
numTies = 0

# Control # of games played
while gameContinue:

    # Print game number message
    gameNum += 1
    print(f"START GAME #{gameNum}\n")

    # Deal card
    playerHand = 0
    card = rng.next_int(13) + 1

    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    elif card == 11:
        card = 10
        print("Your card is a JACK!")
    elif card == 12:
        card = 10
        print("Your card is a QUEEN!")
    elif card == 13:
        card = 10
        print("Your card is a KING!")

    playerHand += card
    print(f"Your hand is: {playerHand}\n")

    # Keep playing current game through prompt
    noWinner = True

    while noWinner:
        print("1. Get another card\n"
            "2. Hold hand\n"
            "3. Print statistics\n"
            "4. Exit\n")

        #Prompt player for input
        option = int(input("Choose an option: "))
        print()
        if option == 1:

            # Deal a card to the dealer
            card = rng.next_int(13) + 1

            if card == 1:
                print("Your card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
            elif card == 11:
                card = 10
                print("Your card is a JACK!")
            elif card == 12:
                card = 10
                print("Your card is a QUEEN!")
            elif card == 13:
                card = 10
                print("Your card is a KING!")

            playerHand += card
            print(f"Your hand is: {playerHand}\n")

            if playerHand == 21:
                # Print winning message
                print("BLACKJACK! You win!\n")
                noWinner = False
                playerWins += 1

            elif playerHand > 21:
                # Print losing message
                print("You exceeded 21! You lose.\n")
                noWinner = False
                dealerWins += 1

        elif option == 2:
            # Deal a card to the dealer
            dealerHand = rng.next_int(11) + 16

            # Compare player hand with dealer hand value
            print(f"Dealer's hand: {dealerHand}")
            print(f"Your hand is: {playerHand}\n")

            if playerHand > dealerHand:
                print("You win!")
                playerWins += 1
                noWinner = False

            elif dealerHand > playerHand:
                if dealerHand > 21:
                    print("You win!\n")
                    playerWins += 1
                    noWinner = False
                else:
                    print("Dealer wins!\n")
                    dealerWins += 1
                    noWinner = False
            else:
                print("It's a tie! No one wins!")
                numTies += 1
                noWinner = False
        elif option == 3:
            print(f"Number of Player wins: {playerWins}")
            print(f"Number of Dealer wins: {dealerWins}")
            print(f"Number of tie games: {numTies}")
            print(f"Total # of games played is: {gameNum - 1}")
            print(f"Percentage of Player wins: {(playerWins/(playerWins + dealerWins + numTies))*100}%\n")
        elif option == 4:
            noWinner = False1
            gameContinue = False
        else:
            print(f"Invalid input!")
            print(f"Please enter an integer value between 1 and 4.")
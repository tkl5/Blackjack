import random

def main():
    print("Welcome to Blackjack\n")

    draw1 = random_draw()
    
    player1_score = calculate_score(draw1)
    if player1_score == 22:
        player1_score = -1
    
    draw2 = random_draw()

    player2_score = calculate_score(draw2)
    if player2_score == 22:
        player2_score = -1

    player_num1 = "1"
    player_num2 = "2"
    player_1output = display_player(draw1, player_num1, player1_score)
    player_2output = display_player(draw2, player_num2, player2_score)
    
    winner = determine_winner(player1_score, player2_score)
    if winner == 2:
        print("Player 2 wins!")
    if winner == 1:
        print("Player 1 wins!")
    if winner == 0:
        print("It's a Draw!")

# Post: Returns two random integers between 1 and 13 inclusive as a list        
def random_draw():
    ranList = []
    
    for i in range(2):
        draw_two = random.randint(1, 13)
        ranList.append(draw_two)
   
    return ranList

# Pre : A list with two random integers
# Post: Returns blackjack int equivalent of score
def calculate_score(ranList):
    points = 0
    scoreDeck = ranList[:]

    for i in range(0, len(scoreDeck)):
        if scoreDeck[i] == 13:
            scoreDeck[i] = 10
            
        if scoreDeck[i] == 12:
            scoreDeck[i] = 10
            
        if scoreDeck[i] == 11:
            scoreDeck[i] = 10
            
        if scoreDeck[i] == 1:
            scoreDeck[i] = 11

    points += sum(scoreDeck)
    return points

# Pre : Takes the integer scores of player 1 and player 2
# Post: Returns 1 or 2, representing which player won by being
#       closer to 21. Returns 0 if a draw.
def determine_winner(player1_score, player2_score):
    if player1_score == player2_score:
        return 0
    
    if player1_score == -1:
        return 2
    
    if (player1_score > player2_score) and player1_score != -1:
        return 1
    
    if (player1_score < player2_score) and player2_score != -1:
        return 2
    
    if player2_score == -1:
        return 1
    
    if player1_score > player2_score:
        return 1
    
    if (player1_score < player2_score) and player2_score != -1:
        return 2
    
# Pre : Takes two random integers as strings from ranList
# Post: Returns the string representing the equivalent card
def card_name(ranList):
    ranList = str(ranList)
    for i in ranList:
        if ranList == '1':
            return 'A'
        
        if ranList == '11':
            return 'J'
        
        if ranList == '12':
            return 'Q'
        
        if ranList == '13':
            return 'K'
        
    ranList = ranList[:]
    return ranList

# Pre : Takes two cards, player number, and his score while calling the card_name function
# Post: Displays player's cards and score
def display_player(ranList, player_num, player_score):
    player = print("Player {}: {} and {}, score {}".format(player_num, card_name(ranList[0]), card_name(ranList[1]), player_score))
    return player
                           
main()

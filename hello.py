from random import randrange
board = [[1,2,3], [4,5,6], [7,8,9]]

def display_board(x):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("| ", x[0][0] , " | ", x[0][1] ," | ",x[0][2]," |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("| ", x[1][0] , " | ", x[1][1] ," | ",x[1][2]," |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print("| ", x[2][0] , " | ", x[2][1] ," | ",x[2][2]," |")
    print("|     |     |     |")
    print("+-----+-----+-----+")


all_numbers = []
def enter_move(board):
   # The function accepts the board's current status, asks the user about their move, 
    try:
        number = int(input("Enter your move: "))
        if number in all_numbers:
            print("numarul a fost deja introdus, reincearca")
            enter_move()
        all_numbers.append(number)
    # checks the input, and updates the board according to the user's decision.
        if number >= 1 and number <= 9:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == number:
                        board[i][j] = "O"
        else:
            print("Numarul este incorect.")
            enter_move(board)
    except:
        print("Trebuie sa introduci un numar.")
        enter_move(board)



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                free_squares.append((i,j))
    return free_squares



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i] == [sign, sign, sign]:
            return "victory"
    for j in range(3):
        x = 0
        for i in range(3):
            if board[i][j] == sign:
                x += 1
            else:
                break
            if x == 3:
                return "victory"    
    for i in range(3):
        x = 0 
        if board[i][i] == sign:
            x += 1
        else:
            break
        if x == 3:
            return "victory"
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return "victory"
    


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_places = make_list_of_free_fields(board)
    count = len(free_places)
    rand_value = randrange(count)
    position_tuple = free_places[rand_value] 
    i = position_tuple[0]
    j = position_tuple[1]
    board[i][j] = "X"

board[1][1] = "X"
for i in range(8):
    display_board(board)
    if i % 2 == 0:
        sign = "O"
        enter_move(board)
    else:
        sign = "X"
        draw_move(board)
    
    # display_board(board)
    if victory_for(board, sign) == "victory":
        print("Victory, player with ", sign , "won the game!")
        display_board(board)
        break
    else:
        if i == 7:
            print("Draw game!")
    







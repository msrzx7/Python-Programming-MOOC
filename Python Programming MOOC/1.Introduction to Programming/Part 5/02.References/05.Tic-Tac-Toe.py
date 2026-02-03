# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):

    if -1 < y < 3 and -1 < x < 3: # updataing boundary for input only 0,1,2 are allowed

        if game_board[y][x] == "": # checking for empty string

            game_board[y][x] = piece # updating string
            return True

        else:
            return False

    else:
        return False

if __name__ == "__main__":
    print(play_turn(game_board,x,y,piece))

### ANOTHER METHOD ###

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or y < 0 or x > 2 or y > 2: # checking the boundary first if doesn't statisfy retruns false
        return False
 
    # Note, that y-coordinate is given first
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
 
    return False
    
def printboard(X, O):
    zero = 'X' if X[0] else('O' if O[0] else 0)
    one = 'X' if X[1] else('O' if O[1] else 1)
    two = 'X' if X[2] else('O' if O[2] else 2)
    three = 'X' if X[3] else('O' if O[3] else 3)
    four = 'X' if X[4] else('O' if O[4] else 4)
    five = 'X' if X[5] else('O' if O[5] else 5)
    six = 'X' if X[6] else('O' if O[6] else 6)
    seven = 'X' if X[7] else('O' if O[7] else 7)
    eigth = 'X' if X[8] else('O' if O[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eigth}")

def checkwin(X, O):
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [3,5,8],
        [1,4,8],
        [2,4,6]
    ]
    for win in wins:
        if(X[win[0]] + X[win[1]] + X[win[2]] == 3):
            print("X win's !!")
            return 1
        elif(O[win[0]] + O[win[1]] + O[win[2]] == 3):
            print("O win's !!")
            return 0
    return -1     
        

if __name__ == "__main__":
    X = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    O = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        printboard(X, O)
        if(turn == 1):
            print("X's turn")
            value = int(input("Enter a value : "))
            X[value] = 1
        else:
            print("O's turn")
            value = int(input("Enter a value : "))
            O[value] = 1
        cwin = checkwin(X, O)
        if(cwin != -1):
            print("Match Over!!")
            break
        turn = 1 - turn 
import random
def place(num,x):
    for i in range(len(x)):
        if x[i] == num:
            pos = x.index(num)
            return x[(pos + 1)]
    return str(num)
def print_grid(move,player,x):
    p_list.extend([move,player])
    grid = ["","-------------\n",
        "|",place(1,p_list),"|",place(2,p_list),"|",place(3,p_list),"|\n",
        "|---+---+---|\n",
        "|",place(4,p_list),"|",place(5,p_list),"|",place(6,p_list),"|\n",
        "|---+---+---|\n",
        "|",place(7,p_list),"|",place(8,p_list),"|",place(9,p_list),"|\n",
        "-------------\n"]
    if x == 2:
        print '\n', ' '.join(grid)
def winner(x,player,xx):
    if ((1 in x and 4 in x and 7 in x)or(1 in x and 2 in x and 3 in x)or(2 in x and 5 in x and 8 in x)or(3 in x and 6 in x and 9 in x)or
    (4 in x and 5 in x and 6 in x)or(7 in x and 8 in x and 9 in x)or(1 in x and 5 in x and 9 in x)or(3 in x and 5 in x and 7 in x)):
        if xx <> 1:
            print '\n'*5,"\'%s\'" %player, " WON!"
        return 1 == 1
def pc_part(listx):
    global pc_move
    for x in range(1,10):
        if x not in p_list:
            listx.append(x)
            if (winner(listx,'Pc',1)) == True:
                del listx[-1]
                pc_move = x
                return 1
            del listx[-1]
def pc_and_player():
    global pc_move,p_list,user_list,pc_list
    replay,draw = 0,0
    while True:
        if replay == 1:
            restart = raw_input("Play again? (yes or no): ")
            if restart == "yes":
                pass
            else:
                return
        else:
            print "\nTicTacToe - Pc vs You", '\n'*2,"PC first move\n"
        replay,pc_move,moves,loop_count,p_list,user_list,pc_list = 0,0,0,0,[],[],[]
        for each in "XXXXX":
            loop_count += 1
            if pc_part(pc_list) or pc_part(user_list) == 1:
                pass
            else:
                while True:
                    pc_move = random.randint(1,9)
                    if pc_move in p_list:
                        continue
                    break
            pc_list.append(pc_move)
            print_grid(pc_move,'O',2)

            if loop_count == 5:
                if winner(user_list,'player',2) == True or winner(pc_list,'Pc',2) == True:
                    pass
                else:
                    print "Draw!"
                replay = 1
                break
            if winner(pc_list,'Pc',2) == True:
                replay = 1
                break
            while True:
                try:
                    moves = int(raw_input("\n\'%s\' Enter a value from 1-9 to make your move: " %each))
                    if moves in p_list or moves < 1 or moves > 9:
                        print "Enter an available number between 1-9"
                        continue
                    break
                except:
                    print "Enter a number"
            user_list.append(moves)
            print_grid(moves,each,1)
            if winner(user_list,'player',1) == True:
                print_grid(moves,each,2)
                winner(user_list,'player',2)
                replay = 1
                break
if __name__ == "__main__":
    pc_and_player()

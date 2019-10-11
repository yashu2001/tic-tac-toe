from IPython.display import clear_output
def replay(): 
    rep=input('do you want to play again yes/no?')
    if(rep=='yes'):
        play_game(p1_name,p2_name,p1_symbol,p2_symbol)
    else:
        print('have a nice day!! thanks for playing')
def check_win(pos_list,p_symbol):
    if(p_symbol==pos_list[0]==pos_list[1]==pos_list[2]):
        return True
    elif(p_symbol==pos_list[3]==pos_list[4]==pos_list[5]):
        return True
    elif(p_symbol==pos_list[6]==pos_list[7]==pos_list[8]):
        return True
    elif(p_symbol==pos_list[0]==pos_list[3]==pos_list[6]):
        return True
    elif(p_symbol==pos_list[1]==pos_list[4]==pos_list[7]):
        return True
    elif(p_symbol==pos_list[2]==pos_list[5]==pos_list[8]):
        return True
    elif(p_symbol==pos_list[0]==pos_list[4]==pos_list[8]):
        return True
    elif(p_symbol==pos_list[2]==pos_list[4]==pos_list[6]):
        return True
    else:
        return False
def play_game(p1_name,p2_name,p1_symbol,p2_symbol):#main part that will call other functions
    #initial board print
    pos_list=[0,1,2,3,4,5,6,7,8]
    used_pos=[]
    board_print(pos_list) #call board_print function and will print the board
    turn=0
    while(turn<=8):
            if(turn%2==0):
                pos=int(input('player one please input your choice'))
                if(pos in used_pos):
                    pos=int(input('please enter a position that is empty'))
                used_pos.append(pos)    
                pos_list[pos]=p1_symbol
                board_print(pos_list)
                if(turn>=4):
                    win_check=check_win(pos_list,p1_symbol)
                    if(win_check):
                        print(p1_name,' wins')
                        replay()
                        break
                turn+=1
            else:
                pos=int(input('player two please input your choice'))
                if(pos in used_pos):
                    pos=int(input('please enter a position that is empty'))
                used_pos.append(pos)    
                pos_list[pos]=p2_symbol
                board_print(pos_list)
                if(turn>=4):
                    win_check=check_win(pos_list,p2_symbol)
                    if(win_check):
                        print(p2_name,' wins')
                        replay()
                        break
                turn+=1
    
def board_print(pos_list): #func to print boards
    clear_output()
    print(f'{pos_list[6]}   |   {pos_list[7]}   |   {pos_list[8]}   ')
    print('    |       |        ')
    print('-----------------------')
    print(f'{pos_list[3]}   |   {pos_list[4]}   |   {pos_list[5]}   ')
    print('    |       |        ')
    print('-----------------------')
    print(f'{pos_list[0]}   |   {pos_list[1]}   |   {pos_list[2]}   ')
    print('    |       |        ')

print(' welcome to tic tac toe by yash \n')
p1_name=input('player one please input your name: ')
p2_name=input('\nplayer two please input your name: ')
p1_symbol=input("\nplayer one please choose 'x' or 'o': ")
if(p1_symbol=='x'):
    p2_symbol='o'
else:
    p2_symbol='x'
print('\nplayer one =',p1_symbol,'\n\nplayer two= ',p2_symbol)
play_game(p1_name,p2_name,p1_symbol,p2_symbol)


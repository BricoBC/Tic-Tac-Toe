import random, sys
arr = ['1','2','3','4','5','6','7','8','9']

def winner():
    global arr
    contador = 1 #Este contador será para sumar cuántos M o # hay
    win = [[0,1,2], [3,4,5],[6,7,8],
    [0,3,6],[1,4,7], [2,5,8], 
    [0,4,8], [2,4,6]]
    is_win_player = []
    is_win_machine = []
    for i in range(9):
        if arr[i] == 'M':
            contador+=1
            is_win_machine.append(i)
        if arr[i] == '#':
            contador+=1
            is_win_player.append(i)
    is_win_machine.sort()
    is_win_player.sort()
    for i in range(len(win)):
        if contador == len(arr):
            print("Quedaron empatados")
            sys.exit()
        if win[i] == is_win_machine:
            print("The winner is the machine")
            sys.exit()
        if win[i] == is_win_player:
            print("The winner is the player")
            sys.exit()

        # print(f'Number: {i}')
        
    


    

def board(arr):
    return f'''+----------------+----------------+----------------+
|                |                |                |                
|                |                |                |
|                |                |                |
|       {arr[0]}        |       {arr[1]}        |       {arr[2]}        |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
+----------------+----------------+----------------+
|                |                |                |                
|                |                |                |
|                |                |                |
|       {arr[3]}        |       {arr[4]}        |       {arr[5]}        |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
+----------------+----------------+----------------+
|                |                |                |                
|                |                |                |
|                |                |                |
|       {arr[6]}        |       {arr[7]}        |       {arr[8]}        |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
+----------------+----------------+----------------+
'''

def player_turn(name):
    global arr
    condition = True
    while condition:
        player = int(input(f"{name} elige un numero: "))-1
        if arr[player] != 'M' and arr[player] != '#':
            arr[player] = '#'
            condition = False
        else:
            print('Elige un lugar disponible...')
    
# Function for put value of machine to arr
def machine_turn():
    global arr
    condition = True
    while condition:
        machine = random.randrange(1,10)
        if arr[machine-1] != 'M' and arr[machine-1] != '#':
            arr[machine-1] = 'M'
            condition = False
        
    print(f"The machine choose the number: {machine}")

def round(name):
    global arr
    #Turno de la máquina
    machine_turn()
    print(board(arr))
    #Se verifica si ya ganó la máquina
    winner()
    #Turno del jugador
    player_turn(name)
    print(board(arr))
    #Se verifica si ya ganó el jugador
    winner()

def play(name):
    for _ in range (9):
        round(name)
        

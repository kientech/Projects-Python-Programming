from random import randint


map = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_map():
    for i in range(0, 9, 3):
        print(map[i], " | ", map[i+1], " | ", map[i+2])
        print("-------------")
print_map()

def empty():
    for i in range(0, 9):
        if map[i] != "X" and map[i] != "O":
            return True


def check_row(select, x1, x2, x3):
    if map[x1] == select and map[x2] == select and map[x3] == select:
        return True
    return False

def check_columns(select, x1, x2, x3):
    if map[x1] == select and map[x2] == select and map[x3] == select:
        return True
    return False

def check_all(select):
    if check_row(select, 0, 1, 2) == True:
        return True
    
    if check_row(select, 3, 4, 5) == True:
        return True
    
    if check_row(select, 6, 7, 8) == True:
        return True

    if check_columns(select, 0, 3, 6) == True:
        return True
    
    if check_columns(select, 1, 4, 7) == True:
        return True
    
    if check_columns(select, 2, 5, 8) == True:
        return True 
    
    if check_columns(select, 0, 4, 8) == True:
        return True 
    
    if check_columns(select, 2, 4, 6) == True:
        return True 
    return False
while empty():
    player = int(input("Enter the cell you want to select ( from 0 to 8 ): "))
    if map[player] == "X" or map[player] == "O":
        print("Selected Cell!!!")
    else:
        map[player] = 'X'
        
    computer = randint(0, 8)
    if map[computer] == "X" or map[computer] == "O":
        break
    
    
    else:
        map[computer] = 'O'
    print_map()
    if check_all("X"):
        win = 'Player'
        break
    elif check_all("O"):
        win = 'Computer'
        break
if win == "":
    print("Invalid")
print(win, "Win")
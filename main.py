from time import sleep


location = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], \
            [1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [1, 0], \
            [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], \
            [3, 5], [3, 4], [3, 3], [3, 2], [3, 1], [3, 0]]

def turn_id_to_location(id):
    return location[id]

def turn_location_to_id(loc):
    for i in range(len(location)):
        if location[i] == loc:
            return i

box1 = 23
box2 = 13
boxes = [1, 2]
front = [0, 1]
cur = 0
animation = True
ans_boxes = []
end = False

def fill_boxes():
    global box1
    global box2
    global boxes
    boxes = [turn_id_to_location(box1), turn_id_to_location(box2)]

def print_map():
    global animation
    if not animation: return
    global cur
    global front
    for i in range(3, -1, -1):
        for j in range(6):
            if cur == turn_location_to_id([i, j]):
                if front == [1, 0]: print("↑", end=" ")
                elif front == [-1, 0]: print("↓", end=" ")
                elif front == [0, 1]: print("→", end=" ")
                else: print("←", end=" ")
            elif [i, j] in boxes:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
    sleep(0.3)

def go():
    global cur
    global front
    cur = turn_location_to_id([turn_id_to_location(cur)[0] + front[0], turn_id_to_location(cur)[1] + front[1]])
    print_map()
    return

def turn_left():
    global cur
    global front
    if front == [1, 0]: front = [0, -1]
    elif front == [-1, 0]: front = [0, 1]
    elif front == [0, 1]: front = [1, 0]
    else: front = [-1, 0]
    print_map()
    return

def turn_right():
    global cur
    global front
    if front == [1, 0]: front = [0, 1] 
    elif front == [-1, 0]: front = [0, -1]
    elif front == [0, 1]: front = [-1, 0]
    else: front = [1, 0]
    print_map()
    return

def turn_180():
    global cur
    global front
    if front == [1, 0]: front = [-1, 0] 
    elif front == [-1, 0]: front = [1, 0]
    elif front == [0, 1]: front = [0, -1]
    else: front = [0, 1]
    print_map()
    return

def rotate():
    global cur
    global front
    if cur in [5, 6, 17, 18]: turn_left()
    elif cur in [11, 12]: turn_right()
    return

def check_box():
    global cur
    global front
    global ans_boxes
    if [turn_id_to_location(cur)[0] + front[0], turn_id_to_location(cur)[1] + front[1]] in boxes:
        ans_boxes = ans_boxes + [turn_location_to_id([turn_id_to_location(cur)[0] + front[0], turn_id_to_location(cur)[1] + front[1]])]
        return True
    return False

def avoid_box():
    global cur
    global front
    global end
    if cur in [0, 1, 2]:
        turn_left()
        if check_box(): 
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_left()
            return
        go()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_180()
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        return
    if cur in [3]:
        turn_left()
        if check_box(): 
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_left()
            return
        go(); go(); turn_right()
        if check_box():
            turn_180()
            return
        go(); turn_left()
        return
    if cur in [4]:
        turn_left()
        if check_box(): 
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_180()
            return
        go(); turn_right()
        if check_box():
            turn_180()
            return
        go(); turn_left()
        return
    if cur in [5]:
        turn_left(); go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        return
    if cur in [6, 7, 8]:
        turn_right()
        if check_box():
            turn_180(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        if check_box():
            turn_right(); go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_right()
            return
        go()
        if check_box():
            turn_right(); go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_left(); go(); turn_180()
            return
        go(); turn_left()
        if check_box():
            turn_right(); go(); turn_left(); go(); turn_right()
            return
        go(); turn_right()
        return
    if cur in [9]:
        turn_right()
        if check_box():
            turn_180(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        if check_box():
            turn_right(); go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_right()
            return
        go()
        if check_box():
            turn_180(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        if check_box():
            turn_180()
            return
        go(); turn_right()
        return
    if cur in [10]:
        turn_right()
        if check_box():
            turn_right(); go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_left(); go(); turn_180()
            return
        go(); turn_left()
        if check_box():
            turn_180()
            return
        go(); turn_right()
        return
    if cur in [11]:
        turn_right()
        if check_box():
            turn_right(); go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_left(); go(); turn_180()
            return
        go(); turn_left()
        if check_box():
            turn_right(); go(); turn_left(); go(); turn_right()
            return
        go(); turn_right()
        return
    if cur in [12, 13, 14]:
        turn_right()
        if check_box():
            turn_180(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        if check_box():
            turn_right(); go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_right()
            return
        go()
        if check_box():
            turn_right();go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_left(); go(); turn_180()
            return
        go(); turn_left()
        if check_box():
            turn_right(); go(); turn_left(); go(); turn_right()
            return
        go(); turn_right()
        return
    if cur in [15]:
        turn_right()
        if check_box():
            turn_180(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        if check_box():
            turn_right(); go(); turn_left(); go(); go(); turn_left(); go(); go(); turn_right()
            return
        go()
        if check_box():
            turn_180(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        if check_box():
            turn_left(); go(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_left()
            return
        go(); turn_right()
        return
    if cur in [16]:
        turn_left(); go(); turn_right()
        if check_box():
            turn_180()
            return
        go(); turn_left()
        return
    if cur in [17]:
        turn_left()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_180()
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        return
    if cur in [18]:
        turn_left(); go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_left()
            return
        go()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_180()
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        return
    if cur in [19, 20]:
        turn_left()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_left()
            return
        go()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_180()
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); turn_left()
            return
        go(); turn_left()
        return
    if cur in [21]:
        turn_left()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_right(); go(); turn_left(); go(); turn_right(); go(); turn_left()
            end = True
            return
        go(); turn_right()
        if check_box():
            turn_left(); go(); turn_right(); go(); go(); turn_right(); go(); go(); turn_left()
            end = True
            return
        go(); go(); turn_right()
        if check_box():
            turn_left()
            end = True
            return
        go(); turn_left()
        end = True
        return
    else:
        end = True
    return
    
def return_home():
    global cur
    global front
    # while cur != 0:
    #     if check_box() or turn_location_to_id([turn_id_to_location(cur)[0] + front[0], turn_id_to_location(cur)[1] + front[1]]) == None:
    #         turn_right()
    #         if check_box() or turn_location_to_id([turn_id_to_location(cur)[0] + front[0], turn_id_to_location(cur)[1] + front[1]]) == None:
    #             turn_180()
    #     elif cur in [0, 11, 12]: go()
    #     else:
    #         turn_right()
    #         if check_box() or turn_location_to_id([turn_id_to_location(cur)[0] + front[0], turn_id_to_location(cur)[1] + front[1]]) == None:
    #             turn_left()
    #         go()
    return


# ---------------- Check one particular box-combination ----------------

# Location:
# 23 22 21 20 19 18
# 12 13 14 15 16 17
# 11 10 09 08 07 06
# 00 01 02 03 04 05

animation = False # True | False

# box1 = 7
# box2 = 15
# fill_boxes()

# print_map()
# while not end and cur != 23:
#     rotate()
#     if check_box(): 
#         avoid_box()
#         continue
#     go()

# return_home()
# print(set(ans_boxes))


# ---------------- Check for every possible box-combination ----------------

for i in range(1, 23):
    for j in range(i + 1, 24): 
        # print(i, j)
        ans_boxes = []
        cur = 0
        front = [0, 1]
        end = False
        if sorted([i, j]) in [[1, 11], [4, 6], [17, 19], [12, 22]]: continue
        boxes = [turn_id_to_location(i), turn_id_to_location(j)]
        while (not end) and (cur != 23):
            rotate()
            if check_box(): 
                avoid_box()
                continue
            go()
        return_home()
        if sorted(list(set(ans_boxes))) != sorted([i, j]): print("Wrong boxes: " + str(i) + " " + str(j))
#         if cur != 0: print("Not back home: " + str(i) + " " + str(j))


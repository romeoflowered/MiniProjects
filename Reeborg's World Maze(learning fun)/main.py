#Reeborg's World Maze(learning fun)
# def move_1():
#     while wall_in_front():
#         turn_left()
#     else:
#         move()
#     while not wall_on_right():
#         turn_right()
#         move()
#
#
# while not at_goal():
#     move_1()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()

clear()
while get_pos_x() != 0:
    move(North)
        
while get_pos_y() != 0:
    move(East)

while True:
    if can_harvest():
        harvest()
        move(North)
    else:
        if get_pos_y() == 0:
            move(East)
        else:
            move(North)
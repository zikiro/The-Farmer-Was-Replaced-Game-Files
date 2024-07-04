clear()
while get_pos_x() != 0:
    move(North)
        
while get_pos_y() != 0:
    move(East)

while True:
    if get_entity_type() == Entities.Grass:
        plant(Entities.Bush)
        move(North)
    elif can_harvest():
        harvest()
        move(North)
    else:
        if get_pos_y() == 0:
            move(East)
            plant(Entities.Bush)
        else:
            move(North)
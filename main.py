while True:
    if get_entity_type() == Entities.Grass:
        plant(Entities.Bush)
    elif can_harvest():
        harvest()
    else:
        if get_pos_y() != 0:
            plant(Entities.Bush)
            move(North)
        elif can_harvest():
            harvest()
            move(North)
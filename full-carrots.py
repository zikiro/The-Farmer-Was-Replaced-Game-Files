clear()
while get_pos_x() != 0:
    move(North)
        
while get_pos_y() != 0:
    move(East)

while True:
    if get_entity_type() == Entities.Grass:
        till()
        trade(Items.Carrot_Seed)
        plant(Entities.Carrots)
        move(North)
    elif can_harvest():
        harvest()
        trade(Items.Carrot_Seed)
        plant(Entities.Carrots)
        move(North)
    else:
        if get_pos_y() == 0:
            move(East)
        else:
            move(North)
# Script settings
shouldClear = True
if shouldClear:
    clear()

while get_pos_y() != 0:
    move(North)
        
while get_pos_x() != 0:
    move(East)

while True:
    if get_entity_type() == Entities.Grass:
        till()
        trade(Items.Pumpkin_Seed)
        plant(Entities.Pumpkin)
        use_item(Items.Water_Tank)
        move(North)
    elif can_harvest() or not get_entity_type():
        harvest()
        trade(Items.Pumpkin_Seed)
        plant(Entities.Pumpkin)
        use_item(Items.Water_Tank)
        move(North)
    else:
        if get_pos_y() == 0:
            move(East)
        else:
            move(North)
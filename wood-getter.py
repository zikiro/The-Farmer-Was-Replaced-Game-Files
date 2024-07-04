# Script settings
shouldClear = False


if shouldClear: 
    clear()

while get_pos_y() != 0:
    move(North)
        
while get_pos_x() != 0:
    move(East)
    
    
def treeOrBush():
    x = get_pos_x()
    y = get_pos_y()
    oddCords = (x % 2) == 1 and (y % 2) == 1
    evenCords = (x % 2) == 0 and (y % 2) == 0
    isTreePos = oddCords or evenCords

    if can_harvest():
        harvest()
    else:
        return
    if isTreePos:
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)

while True:
    if get_pos_y() != 0:
        treeOrBush()
        move(North)
    else: 
        move(East)
        treeOrBush()
        move(North)
    
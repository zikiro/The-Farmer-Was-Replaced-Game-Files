clear()

x = get_pos_x()
y = get_pos_y()

while x != 0:
    move(North)
        
while y != 0:
    move(East)
    
    
def treeOrHay():
    if can_harvest():
        harvest()
    else:
        return
    if get_pos_x() != 1 and get_pos_y() != 1:
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)

while True:
    if get_pos_y() != 0:
        treeOrHay()
        move(North)
    else: 
        move(East)
        treeOrHay()
        move(North)
    
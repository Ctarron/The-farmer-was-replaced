def go_to(x, y):
    world_size = get_world_size()
    distance_x = x - get_pos_x()
    distance_y = y - get_pos_y()
    
    if distance_x > 0:
        direction_x = East 
    else: 
        direction_x = West
    if distance_y > 0:
        direction_y = North  
    else:
        direction_y = South

    for i in range(abs(distance_x)):
        if get_pos_x() == world_size and direction_x == East:
            move(West)
        elif get_pos_x() == 0 and direction_x == West:
            move(East)
        else:
            move(direction_x)

    for i in range(abs(distance_y)):
        if get_pos_y() == world_size and direction_y == North:
            move(South)
        elif get_pos_y() == 0 and direction_y == South:
            move(North)
        else:
            move(direction_y)
		
def calculate_distance(point1, point2):
	x1, y1 = point1
	x2, y2 = point2
	return abs(x2 - x1) + abs(y2 - y1)
def do_1_maze(rounds=1):
	directions = [North, East, South, West]
	i = 1
	while True:
		while move(directions[i]):
			if get_entity_type() != Entities.Hedge:
				harvest()
				go_to(0,0)
				return
			if move(directions[(i + 1) % 4]) == True:
				i = (i + 2) % 4
			if get_entity_type() != Entities.Hedge:
				harvest()
				go_to(0,0)
		i = (i - 1) % 4

def do_maze(x, y, visited, path):
	if (x, y) in visited:
		return False
	
	visited.add((x, y))
	path.append((x, y))
	
	if get_entity_type() == Entities.Treasure:
		return True
	
	for direction in [North, East, South, West]:
		if move(direction):
			if do_maze(get_pos_x(), get_pos_y(), visited, path):
				return True
			move_back(direction)
	
	path.pop()
	return False

def move_back(direction):
	if direction == North:
		move(South)
	elif direction == East:
		move(West)
	elif direction == South:
		move(North)
	elif direction == West:
		move(East)

def create_maze(rounds=1):
	harvest()
	plant(Entities.Bush)
	while not can_harvest():
		do_fertilizer()
	while get_entity_type() == Entities.Bush:
		do_fertilizer()

	if rounds > 300:
		rounds = 300
	
	for i in range(rounds):
		visited = set()
		path = []
		i = 0
		
		if do_maze(get_pos_x(), get_pos_y(), visited, path):
			rounds -= 1
			if rounds > 0:
				while get_entity_type() == Entities.Treasure:
					do_fertilizer()
				continue
			harvest()
			go_to(0, 0)
			return
def do_maze():
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
				return
		i = (i - 1) % 4

def create_maze():
	harvest()
	plant(Entities.Bush)
	while not can_harvest():
		do_fertilizer()
	while get_entity_type() == Entities.Bush:
		do_fertilizer()
	do_maze()
def do_column_old(crop, c=1):
	r = 0
	for i in range(c):
		if get_entity_type() == Entities.Sunflower:
			harvest_sunflower()
		do_water()
		if get_entity_type() != None:
			while not can_harvest():
				do_fertilizer()
			harvest()
		crop(r)
		r += 1
		move(North)
		while get_pos_y() != 0:
			if get_entity_type() == Entities.Sunflower:
				harvest_sunflower()
			do_water()
			if get_entity_type() != None:
				while not can_harvest():
					do_fertilizer()
				harvest()
			crop(r)
			r += (get_world_size()%2) +1
			move(North)
		r += 1
		move(East)
		
def do_pumpkin_old(r):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Pumpkin_Seed)
	plant(Entities.Pumpkin)

def do_carrot_old(r):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Carrot_Seed)
	plant(Entities.Carrots)

def do_grass_old(r):
	plant(Entities.Grass)
		
def do_wood_old(r):
	if r % 2 == 0:
		plant(Entities.Tree)
	else: 
		plant(Entities.Bush)

def do_fertilizer_old():
	trade(Items.Fertilizer)
	use_item(Items.Fertilizer)

def do_water_old():
	while get_water() != 1:
		if not use_item(Items.Water_Tank):
			trade(Items.Empty_Tank, 4)

def do_sunflower_old(r=1):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Sunflower_Seed)
	plant(Entities.Sunflower)
	
def do_full_sunflower_field_old(size_x = get_world_size(), size_y = get_world_size()):
	sunflowers = {}
	for i in range(size_x):
		for j in range(size_y):
			harvest()
			do_sunflower()
			petals = measure() 
			if petals not in sunflowers:
				sunflowers[petals] = []
			sunflowers[petals].append([get_pos_x(),get_pos_y()])
			move(North)
		move(East)
	
	while sunflowers:
		max_key = max(sunflowers)
		max_petals = sunflowers.pop(max_key)
		while max_petals:
			next_coords = max_petals.pop()
			go_to(next_coords[0], next_coords[1])
			while not can_harvest():
				do_fertilizer()
			harvest()
	go_to(0,0)
	
def do_maze_old(x, y, visited, path):
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

def move_back_old(direction):
	if direction == North:
		move(South)
	elif direction == East:
		move(West)
	elif direction == South:
		move(North)
	elif direction == West:
		move(East)

def create_maze_old(rounds=1):
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
			
def do_cactus_old(r=1):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Cactus_Seed)
	plant(Entities.Cactus)

def sort_neighbours_old():
	size = measure()
	directions = [North, East, South, West]
	i = 0
	while i < 4:
		n_size = measure(directions[i])
		if n_size == None:
			pass
		elif (i < 2 and n_size < size) or (i > 1 and n_size > size):
			swap(directions[i])
			size = n_size
			i = 0
		i += 1
		

def farm_cactus_old(rounds=1):
	go_to(0,0)
	
	rounds -= 1
	for i in range(rounds):
		move(North)
		do_cactus()
		move(South)
		move(East)
		do_cactus()
		move(West)
		do_cactus()
		sort_neighbours()
		while not can_harvest():
			do_fertilizer()
		harvest()

def do_dino_old(r):
	trade(Items.Egg)
	use_item(Items.Egg)
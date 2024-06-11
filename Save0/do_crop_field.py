def do_hay():
	passive_upgrade(Unlocks.Grass)
	size = get_world_size()
	
	for i in range(size):
		for j in range(size):
			do_water()
			while not can_harvest():
				do_fertilizer()
			harvest()
			plant(Entities.Grass)
			move(North)
		move(East)

def do_wood():
	passive_upgrade(Unlocks.Trees)
	size = get_world_size()
	r = 0
	for i in range(size):
		for j in range(size):
			do_water()
			while not can_harvest():
				do_fertilizer()
			harvest()
			if num_unlocked(Unlocks.Trees) != 0 and r % 2 == 0:
				plant(Entities.Tree)
			else: 
				plant(Entities.Bush)
			r += (size % 2) +1
			move(North)
		r += 1
		move(East)
		
def do_carrot():
	if num_unlocked(Unlocks.Carrots) == 0:
		buy_upgrade(Unlocks.Carrots)
	passive_upgrade(Unlocks.Carrots)
	size = get_world_size()
	buy_stock(Items.Carrot_Seed, size * size)
	for i in range(size):
		for j in range(size):
			do_water()
			while not can_harvest():
				do_fertilizer()
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrots)
			move(North)
		move(East)
	
def do_sunflower():
	passive_upgrade(Unlocks.Sunflowers)
	size = get_world_size()
	buy_stock(Items.Sunflower_Seed, size * size)
	sunflowers = {}
	for i in range(size_x):
		for j in range(size_y):
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
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

def do_pumpkin():
	if num_unlocked(Unlocks.Pumpkins) == 0:
		buy_upgrade(Unlocks.Pumpkins)
	passive_upgrade(Unlocks.Pumpkins)
	size = get_world_size()
	buy_stock(Items.Pumpkin_Seed, size * size)
	for i in range(size):
		for j in range(size):
			do_water()
			while not can_harvest():
				do_fertilizer()
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)

def do_water():
	while get_water() != 1:
		if not use_item(Items.Water_Tank):
			trade(Items.Empty_Tank, 4)
			return False
	return True
	
def do_fertilizer():
	if num_unlocked(Unlocks.Fertilizer) == 0:
		buy_upgrade(Unlocks.Fertilizer)
	if num_items(Items.Fertilizer) == 0:
		buy_stock(Items.Fertilizer, 1)
	return use_item(Items.Fertilizer)

def create_maze(amount=1):
	if num_unlocked(Unlocks.Mazes) == 0:
		buy_upgrade(Unlocks.Mazes)
	passive_upgrade(Unlocks.Mazes)
	harvest()
	plant(Entities.Bush)
	while not can_harvest():
		do_fertilizer()
		
	size = get_world_size()
	expected = 0
    rounds = 0

    while expected < amount:
        expected += (size**2)
        rounds += 1

	if rounds > 300:
		rounds = 300
	
	buy_stock(Items.Fertilizer, rounds * 10 - num_items(Items.Fertilizer))
	
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

def sort_neighbours():
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
		

def do_cactus(amount=1):
	if num_unlocked(Unlocks.Cactus) == 0:
		buy_upgrade(Unlocks.Cactus)
	passive_upgrade(Unlocks.Cactus)
	go_to(0,0)
	
	size = get_world_size()
	expected = 0
    rounds = 0

    while expected < amount:
        expected += (size*3)
        rounds += 1
	
	buy_stock(Items.Cactus_Seed, rounds * 3)
	rounds -= 1
	for i in range(rounds):
		move(North)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		move(South)
		move(East)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		move(West)
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		sort_neighbours()
		while not can_harvest():
			do_fertilizer()
		harvest()

def do_dino():
	if num_unlocked(Unlocks.Dinosaurs) == 0:
		buy_upgrade(Unlocks.Dinosaurs)
	passive_upgrade(Unlocks.Dinosaurs)
	buy_stock(Items.Egg,1)
	use_item(Items.Egg)
	harvest()
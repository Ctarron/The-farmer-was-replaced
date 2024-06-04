
def do_sunflower(r=1):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Sunflower_Seed)
	plant(Entities.Sunflower)

def harvest_sunflower():
	#Usar siempre a la izquierda
	size = get_world_size()
	x = 0
	move(East)
	while get_pos_x() != 0:
		if get_entity_type() != Entities.Sunflower:
			break
		x += 1
		move(East)
	
	go_to(0,0)
	
	sunflowers = {}
	
	for i in range(x):
		while measure() == None:
			move(North)
			if get_pos_y() == 0:
				move(East)
				
		petals = measure() 
		if not petals in sunflowers:
			sunflowers[petals] = []
		sunflowers[petals].append([get_pos_x(),get_pos_y()])
		move(North)
		while get_pos_y() != 0:
			if measure() == None:
				move(North)
				continue
			petals = measure() 
			if not petals in sunflowers:
				sunflowers[petals] = []
			sunflowers[petals].append([get_pos_x(),get_pos_y()]) 
			move(North)
		move(East)
	while sunflowers:
		max_key = max(sunflowers)
		if not sunflowers[max_key]:
			sunflowers.pop(max_key)
			continue
		max_petals = sunflowers[max_key].pop()
		go_to(max_petals[0], max_petals[1])
		harvest()
	go_to(0,0)
	
def do_full_sunflower_field(size_x = get_world_size(), size_y = get_world_size()):
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
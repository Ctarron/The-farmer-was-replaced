def do_sunflower(r=1):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Sunflower_Seed)
	plant(Entities.Sunflower)
	
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
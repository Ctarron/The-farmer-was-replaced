def do_cactus(r=1):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Cactus_Seed)
	plant(Entities.Cactus)

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
		

def farm_cactus(rounds=1):
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
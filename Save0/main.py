

	
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

def do_column(crop, c=1):
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
			r += 1
			move(North)
		r += 1
		move(East)

def un_till():
	if get_ground_type() == Grounds.Soil:
			till()


harvest()
go_to(0,0)

clear()

while True:
	#do_column(do_pumpkin, 8)
	#do_column(do_carrot, 8)
	#do_full_sunflower_field()
	create_maze()
	continue
	
	
	do_full_sunflower_field()
	
	do_column(do_pumpkin, 8)
	
	do_column(do_grass, 4)
	do_column(do_wood, 4)

	do_column(do_grass, 8)
	
	create_maze()
	
	do_column(do_carrot, 4)
	do_column(do_grass, 2)
	do_column(do_wood, 2)
	
		
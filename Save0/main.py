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
			r += (get_world_size()%2) +1
			move(North)
		r += 1
		move(East)

def un_till():
	if get_ground_type() == Grounds.Soil:
			till()


harvest()
go_to(0,0)

clear()

farm_cactus(500)

while True:
	go_to(0,0)
	create_maze(5)
	do_full_sunflower_field()
	
	do_column(do_pumpkin, 10)
	
	do_column(do_grass, 4)
	do_column(do_wood, 6)
	
	do_column(do_carrot, 5)
	do_column(do_grass, 2)
	do_column(do_wood, 3)	
	
	do_column(do_grass, 10)
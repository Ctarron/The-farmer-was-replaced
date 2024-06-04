def do_pumpkin(r):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Pumpkin_Seed)
	plant(Entities.Pumpkin)

def do_carrot(r):
	if get_ground_type() != Grounds.Soil:
		till()
	trade(Items.Carrot_Seed)
	plant(Entities.Carrots)

def do_grass(r):
	plant(Entities.Grass)
		
def do_wood(r):
	if r % 2 == 0:
		plant(Entities.Tree)
	else: 
		plant(Entities.Bush)
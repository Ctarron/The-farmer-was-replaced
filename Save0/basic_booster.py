def do_fertilizer():

	trade(Items.Fertilizer)
	use_item(Items.Fertilizer)

def do_water():
	while get_water() != 1:
		if not use_item(Items.Water_Tank):
			trade(Items.Empty_Tank, 4)
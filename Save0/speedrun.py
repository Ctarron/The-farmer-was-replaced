def do_speedrun():
	while not passive_upgrade(Unlocks.Speed):
		while not can_harvest():
			pass
		harvest()
	while not passive_upgrade(Unlocks.Plant):
		while not can_harvest():
			pass
		harvest()
	buy_upgrade(Unlocks.Leaderboard)

def buy_stock(stock, n=1):
	cost = get_cost(stock)
	for item in cost: 
        amount = cost[item]
		if num_items(item) < amount * n:
			farm_item(item, amount * n)
	trade(stock,n)
 
def buy_upgrade(upgrade):
	cost = get_cost(upgrade)
	if cost == None:
		return False  # Already at max level
    for item in cost: 
        amount = cost[item]
		if num_items(item) < amount:
			farm_item(item, amount)
	unlock(upgrade)

def passive_upgrade(upgrade):
	cost = get_cost(upgrade)
	if cost == None:
		return False  # Already at max level
    for item in cost:
        amount = cost[item] 
		if num_items(item) < amount:
			return False
	unlock(upgrade)
	return True

def farm_item(item, amount):
	passive_upgrade(Unlocks.Speed)
	passive_upgrade(Unlocks.Expand)
	
	size = get_world_size()
	go_to(0, 0)
	
	if item == Items.Hay:
		while num_items(item) < amount:
			do_hay()
	elif item == Items.Wood:
		while num_items(item) < amount:
			do_wood()
	elif item == Items.Carrot:
		while num_items(item) < amount:
			do_carrot()
	elif item == Items.Power:
		while num_items(item) < amount * 1.5:
			do_sunflower()
	elif item == Items.Pumpkin:
		while num_items(item) < amount:
			do_pumpkin()
	elif item == Items.Gold:
		while num_items(item) < amount:
			create_maze(amount)
	elif item == Items.Cactus:
		while num_items(item) < amount:
			do_cactus()
	elif item == Items.Bones:
		while num_items(item) < amount:
			do_dino()
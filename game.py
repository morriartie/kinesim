import oblib as o

def create_ship():
	part1 = []		
	print("------------------")
	part1.append(input("Ship name: "))
	part1.append(input("Volume: "))
	part1.append(input("Lenght: "))
	part1.append(input("Mass: "))
	print("------------------")
	# engines 
	part2 = []	
	print("Main thruster:")
	part2.append(input("  L weight: "))	
	part2.append(input("  L force: "))
	print("------------------")
	## left up	
	left_up = []	
	ans = input("Add engine on left up(y/n): ")	
	print("------------------")
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		prt = []	
		prt.append(input("Distance from center of mass: "))
		prt.append(input("Force: "))
		left_up.append(prt)
		ans = input("Add another on left up(y/n): ")
		print("------------------")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	## right up	
	right_up = []	
	ans = input("Add engine on right up(y/n): ")	
	print("------------------")
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		prt = []
		prt.append(input("Distance from center of mass: "))
		prt.append(input("Force: "))
		right_up.append(prt)		
		ans = input("Add another on right up(y/n): ")
		print("------------------")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	## left down	
	left_down = []
	ans = input("Add engine on left down(y/n): ")	
	print("------------------")
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		prt = []
		prt.append(input("Distance from center of mass: "))
		prt.append(input("Force: "))
		left_down.append(prt)
		ans = input("Add another on left down(y/n): ")
		print("------------------")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	## right down	
	right_down = []
	ans = input("Add engine on right down(y/n): ")	
	print("------------------")	
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		prt = []
		prt.append(input("Distance from center of mass: "))
		prt.append(input("Force: "))
		right_down.append(prt)		
		ans = input("Add another on right down(y/n): ")
		print("------------------")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	# positon
	print("Spawn at:") 
	posx = input("  L x: ")
	posy = input("  L y: ")
	print("------------------")
	orientation = input("Orientation(*pi): ")
	print("------------------")
	# setting variables
	# pt 1	
	ship = o.Ship(part1[0],part1[1],part1[2],part1[3])
	# pt 2	
	ship.engine_power = part2[0]
	ship.engine_weight = part2[1]
	# lu
	ship.left_f_engine_power = []
	ship.left_f_eng_dist_from_cm = []	
	for i in range(len(left_up)):
		ship.left_f_engine_power.append(left_up[i][1])
		ship.left_f_eng_dist_from_cm.append(left_up[i][0])	
	# ru
 	ship.right_f_engine_power = []
	ship.right_f_eng_dist_from_cm = []	
	for i in range(len(right_up)):
		ship.right_f_engine_power.append(right_up[i][1])
		ship.right_f_eng_dist_from_cm.append(right_up[i][0])		
	# ld
	ship.left_b_engine_power = []
	ship.left_b_eng_dist_from_cm = []	
	for i in range(len(left_down)):
		ship.left_b_engine_power.append(left_down[i][1])
		ship.left_b_eng_dist_from_cm.append(left_down[i][0])	
	# rd
	ship.right_b_engine_power = []
	ship.right_b_eng_dist_from_cm = []	
	for i in range(len(right_down)):
		ship.right_b_engine_power.append(right_down[1])
		ship.right_b_eng_dist_from_cm.append(right_down[0])	
	# spawn
	ship.pos_x = posx
	ship.pos_y = posy
	ship.orientation = orientation




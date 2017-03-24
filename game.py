import oblib as o

def create_ship():
	input("Ship name: ")
	input("Volume: ")
	input("Lenght: ")
	input("Mass: ")
	# engines 
	input("Main thruster:")
	input("  L weight: ")
	input("  L force: ")
	## left up	
	ans = input("Add engine on left up?")	
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		input("Distance from center of mass: ")
		input("Force: ")
		ans = input("Add another on left up?")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	## right up	
	ans = input("Add engine on right up?")	
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		input("Distance from center of mass: ")
		input("Force: ")
		ans = input("Add another on right up?")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	## left down	
	ans = input("Add engine on left down?")	
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		input("Distance from center of mass: ")
		input("Force: ")
		ans = input("Add another on left down?")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	## right down	
	ans = input("Add engine on right down?")	
	if(ans.lower() == "y"):
		ans = True
	else:
		ans = False 
	while(ans):
		input("Distance from center of mass: ")
		input("Force: ")
		ans = input("Add another on right down?")
		if(ans.lower() == "y"):
			ans = True
		else:
			ans = False
	# positon
	input("Spawn at:") #v
	input("  L x: ")
	input("  L y: ")
	input("Orientation ")

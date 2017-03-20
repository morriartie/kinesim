from math import sin
from math import cos
from math import pi as PI

class Ship():
	ship_list = []
	ship_count = 0
	def __init__(self,alias,volume,length,mass):
		# info	########################	
		self.ship_id = Ship.ship_count
		self.alias = str(alias)
		# structure ####################
		self.ship_length = length # m
		self.total_volume = volume # m3
		self.volume = self.total_volume # m3
		self.total_mass = mass # kg
		self.mass = self.total_mass # kg
		self.hull_res = 100.0
		# cinematic ####################
		self.pos_x = 0 # m
		self.pos_y = 0 # m
		self.speed_x = 0 # m/s
		self.speed_y = 0 # m/s
		self.acc_x = 0 # m/s^2
		self.acc_y = 0 # m/s^2
		#		
		self.moment_of_inertia = (1/3.0)*self.mass*(self.ship_length**2)		
		self.orientation = 0 # *pi
		self.angular_speed = 0
		self.angular_acc = 0		
		# engine #######################
		## forward
		self.throttle = 0	
		self.engine_power = 30 # N 
		## left	front
		self.left_f_throttle = [0]
		self.left_f_engine_power = [5] # N			
		# distance from the center of mass
		self.left_f_eng_dist_from_cm = [self.ship_length/2.0]		
		## right front		
		self.right_f_throttle = [0]
		self.right_f_engine_power = [5] # N	
		# distance from the center of mass
		self.right_f_eng_dist_from_cm = [self.ship_length/2.0]		
		## left	back
		self.left_b_throttle = [0]
		self.left_b_engine_power = [5] # N			
		# distance from the center of mass
		self.left_b_eng_dist_from_cm = [self.ship_length/2.0]		
		## right back		
		self.right_b_throttle = [0]
		self.right_b_engine_power = [5] # N	
		# distance from the center of mass
		self.right_b_eng_dist_from_cm = [self.ship_length/2.0]		
		# updating #####################
		Ship.ship_list.append(self)
		Ship.ship_count += 1		
	# core setters #########################	
	def set_pos(self,newposx,newposy):
		self.pos_x = int(newposx)
		self.pos_y = int(newposy)
	
	def set_speed(self,newspeed_x,newspeed_y):
		self.speed_x = int(newspeed_x)
		self.speed_y = int(newspeed_y)	

	def set_orientation(self,newori_pi):
		if(newori_pi>=(-1) and newori_pi<=1):
			self.orientation = newori_pi		 
		else:
			self.orientation = newori_pi%2

	def set_throttle(self,newt):
		if(newt<0):
			newt=0		
		elif(newt>100):
			newt=100
		self.throttle = newt

	def set_throttle_left_f(self,n,newt):
		if(newt<0):
			newt=0		
		elif(newt>100):
			newt=100
		self.left_f_throttle[n] = newt

	def set_throttle_right_f(self,n,newt):
		if(newt<0):
			newt=0		
		elif(newt>100):
			newt=100
		self.right_f_throttle[n] = newt	

	def set_throttle_left_b(self,n,newt):
		if(newt<0):
			newt=0		
		elif(newt>100):
			newt=100
		self.left_b_throttle[n] = newt

	def set_throttle_right_b(self,n,newt):
		if(newt<0):
			newt=0		
		elif(newt>100):
			newt=100
		self.right_b_throttle[n] = newt	


	# calcs ################################
	def update_acc(self):
		acc = self.engine_power*(self.throttle/100.0)/self.mass	
		self.acc_x = acc*cos(self.orientation*PI)
		self.acc_y = acc*sin(self.orientation*PI)

	def update_speed(self):  
		self.speed_x += self.acc_x
		self.speed_y += self.acc_y				

	def update_pos(self):
		self.pos_x += self.speed_x
		self.pos_y += self.speed_y
	
	# angular #
	def update_ang_acc(self):
		net_torque = 0
		# left	front
		for i in range(len(self.left_f_engine_power)):
			net_torque += self.left_f_engine_power[i]*self.left_f_throttle[i]*self.left_f_eng_dist_from_cm[i]
		
		# right	front	
		for i in range(len(self.right_f_engine_power)): 				
			net_torque -= self.right_f_engine_power[i]*self.right_f_throttle[i]*self.right_f_eng_dist_from_cm[i]
		# left	back
		for i in range(len(self.left_b_engine_power)): 				
			net_torque -= self.left_b_engine_power[i]*self.left_b_throttle[i]*self.left_b_eng_dist_from_cm[i]
		
		# right	back	
		for i in range(len(self.right_b_engine_power)): 				
			net_torque += self.right_b_engine_power[i]*self.right_b_throttle[i]*self.right_b_eng_dist_from_cm[i]
		# with I
		self.angular_acc = net_torque/self.moment_of_inertia

	def update_ang_speed(self):
		self.angular_speed += self.angular_acc

	def update_ang_pos(self):
		newori = self.orientation + self.angular_speed
		self.set_orientation(newori)
	
	# info #################################
	def show_hud(self):
		print("orientation: "+str(self.orientation)+"*pi")
		print("throttle: "+str(self.throttle)+"%")
		print("current engine force: "+str((self.throttle/100.0)*self.engine_power)+" N")
		print("pos:")
		print("x: "+str(self.pos_x)+" y: "+str(self.pos_y))
		print("speed:")
		print("x: "+str(self.speed_x)+" m/s |y: "+str(self.speed_y)+" m/s")
		print("acceleration:")
		print("x: "+str(self.acc_x)+" m/s^2 |y: "+str(self.acc_y)+" m/s^2")
	
	def show_engines(self):
		print("Engines: ")
		print("L front:")
		print("    L left:")
		for i in range(len(self.left_f_engine_power)):
			throttle = self.left_f_throttle[i]
			position = self.left_f_eng_dist_from_cm[i]
			max_force = self.left_f_engine_power[i]
			force = (throttle/100.0)*max_force
			print("        index: "+str(i))			
			print("        throttle: "+str(throttle)+"%")
			print("        position: "+str(position)+"m")			
			print("        force: "+str(force)+"N")
			print("        max force: "+str(max_force)+"N")
			print("        ---")					
		print("    L right:")
		for i in range(len(self.right_f_engine_power)):
			throttle = self.right_f_throttle[i]
			position = self.right_f_eng_dist_from_cm[i]
			max_force = self.right_f_engine_power[i]
			force = (throttle/100.0)*max_force
			print("        index: "+str(i))			
			print("        throttle: "+str(throttle)+"%")
			print("        position: "+str(position)+"m")			
			print("        force: "+str(force)+"N")
			print("        max force: "+str(max_force)+"N")
			print("        ---")					
		print("L back:")
		print("    L left:")
		for i in range(len(self.left_b_engine_power)):
			throttle = self.left_b_throttle[i]
			position = self.left_b_eng_dist_from_cm[i]
			max_force = self.left_b_engine_power[i]
			force = (throttle/100.0)*max_force
			print("        index: "+str(i))			
			print("        throttle: "+str(throttle)+"%")
			print("        position: "+str(position)+"m")			
			print("        force: "+str(force)+"N")
			print("        max force: "+str(max_force)+"N")
			print("        ")					
		print("    L right:")
		for i in range(len(self.right_b_engine_power)):
			throttle = self.right_b_throttle[i]
			position = self.right_b_eng_dist_from_cm[i]
			max_force = self.right_b_engine_power[i]
			force = (throttle/100.0)*max_force
			print("        index: "+str(i))			
			print("        throttle: "+str(throttle)+"%")
			print("        position: "+str(position)+"m")			
			print("        force: "+str(force)+"N")
			print("        max force: "+str(max_force)+"N")
			print("        ---")					

	# tools ################################
	def reset(self):
		self.volume = self.total_volume
		self.mass = self.total_mass
		self.pos_x = 0
		self.pos_y = 0
		self.speed_x = 0
		self.speed_y = 0
		self.acc_x = 0
		self.acc_y = 0
		self.orientation = 0
		self.angular_speed = 0
		self.angular_acc = 0		
		self.throttle = 0
		self.left_throttle = 0
		self.right_throttle = 0	

##### lib funcs ################################
def pass_time(time):
	for i in range(len(Ship.ship_list)):
		for j in range(time):
			# acc			
			Ship.ship_list[i].update_acc()
			Ship.ship_list[i].update_ang_acc()
			# spd				
			Ship.ship_list[i].update_speed()
			Ship.ship_list[i].update_ang_speed()
			# pos			
			Ship.ship_list[i].update_pos()
			Ship.ship_list[i].update_ang_pos()

def show_positions():
	for i in range(len(Ship.ship_list)):
		s = Ship.ship_list[i]		
		x = int(s.pos_x)
		y = int(s.pos_y)
		print("("+str(s.orientation)+"pi,"+str(x)+","+str(y)+")["+str(s.ship_id)+":"+s.alias+"]")

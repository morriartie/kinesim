import oblib as ob
import game as ga
import sqlite3 as sql

dbname = "world.db"
database = None
cur = None
con = None

ships = []

def load_db():
	global dbname
	global database
	global con
	global dbcursor
	#
	con = sql.connect(dbname)
	cur = con.cursor()

def load_objects():
	global ships
	#
	select = "SELECT (SELECT count() FROM Ships) AS count"
	cur.execute(select)
	con.commit()
	n_of_ships = cur.fetchone()[0]
	#
	for i in range(n_of_ships):
		ship_id = 
		alias = 
		owner = 		
		ship_length = 
		total_volume = 
		volume = 
		total_mass = 
		mass = 
		hull_res = 
		pos_x = 
		pos_y = 
		speed_x = 
		speed_y = 
		acc_x = 
		acc_y = 
		res_speed = 
		res_acc = 
		moment_of_inertia = 		
		orientation = 
		angular_speed = 
		angular_acc = 		
		throttle = 	
		engine_power =  
		engine_weight = 
		left_f_throttle = 
		left_f_engine_power = 			
		left_f_eng_dist_from_cm = 		
		right_f_throttle = 
		right_f_engine_power = 	
		right_f_eng_dist_from_cm = 		
		left_b_throttle = 
		left_b_engine_power = 			
		left_b_eng_dist_from_cm = 		
		right_b_throttle = 
		right_b_engine_power = 	
		right_b_eng_dist_from_cm = 	
	
		 
	

#!/usr/bin/python
import os
import sys
import socket
from time import sleep
from random import randint
import sqlite3

dbname = "world.db"
database = None
dbcursor = None
con = None

commands = []
online_user = None

ships = []
owners = []



s = None
c = None
hp = None 

def load_db():
	global dbname
	global database
	global con
	global dbcursor
	con = sqlite3.connect(dbname)
	dbcursor = con.cursor()

def load_comm_list():
	global commands
	commands = open("commandlist").read().split('\n')

def order(vec,ref):
	return [x for (x,y) in sorted(zip(vec,ref))]

################################################
def command(comm):
	if(comm in commands):
		output = exec_command(comm)
		return (True,output)
	else:
		return (False,'')

def exec_command(command):
	global dbcursor
	global con
	global online_user	
	# up left	
	if(command=="set-throttle-ul"):
		colname = "LF_Throttle"
		sendm("index: ")
		inds = recvm()
		inds = str(int(inds))
		sendm("value: ")
		vals = recvm()
		# getting values
		select = "SELECT %s FROM Ships WHERE Owner='%s'"%(colname,str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		# updating value
		values = str(data[0]).split(',')
		for i in range(len(values)):
			if(i==inds):
				values[i] = vals		
		# setting values
		values = ','.join(values)
		select = "UPDATE Ships SET %s=%s WHERE Owner='%s'"%(colname,values,str(online_user))
		dbcursor.execute(select)
		con.commit()
	# up right	
	elif(command=="set-throttle-ur"):
		colname = "RF_Throttle"
		sendm("index: ")
		inds = recvm()
		inds = str(int(inds))
		sendm("value: ")
		vals = recvm()
		# getting values
		select = "SELECT %s FROM Ships WHERE Owner='%s'"%(colname,str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		# updating value
		values = str(data[0]).split(',')
		for i in range(len(values)):
			if(i==inds):
				values[i] = vals		
		# setting values
		values = ','.join(values)
		select = "UPDATE Ships SET %s=%s WHERE Owner='%s'"%(colname,values,str(online_user))
		dbcursor.execute(select)
		con.commit()
	# down left	
	elif(command=="set-throttle-dl"):
		colname = "LB_Throttle"
		sendm("index: ")
		inds = recvm()
		inds = str(int(inds))
		sendm("value: ")
		vals = recvm()
		# getting values
		select = "SELECT %s FROM Ships WHERE Owner='%s'"%(colname,str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		# updating value
		values = str(data[0]).split(',')
		for i in range(len(values)):
			if(i==inds):
				values[i] = vals		
		# setting values
		values = ','.join(values)
		select = "UPDATE Ships SET %s=%s WHERE Owner='%s'"%(colname,values,str(online_user))
		dbcursor.execute(select)
		con.commit()
	# down right	
	elif(command=="set-throttle-dr"):
		colname = "RB_Throttle"
		sendm("index: ")
		inds = recvm()
		inds = str(int(inds))
		sendm("value: ")
		vals = recvm()
		# getting values
		select = "SELECT %s FROM Ships WHERE Owner='%s'"%(colname,str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		# updating value
		values = str(data[0]).split(',')
		for i in range(len(values)):
			if(i==inds):
				values[i] = vals		
		# setting values
		values = ','.join(values)
		select = "UPDATE Ships SET %s=%s WHERE Owner='%s'"%(colname,values,str(online_user))
		dbcursor.execute(select)
		con.commit()
	elif(command=="set-throttle"):
		sendm("throttle: ")
		inp = recvm()
		select="UPDATE Ships SET Throttle=%s WHERE Owner='%s'"%(str(inp),str(online_user))
		dbcursor.execute(select)
		con.commit()

	elif(command=="get-throttle-ul"):
		select="SELECT LF_Throttle FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-throttle-ur"):
		select="SELECT RF_Throttle FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-throttle-dl"):
		select="SELECT LB_Throttle FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-throttle-dr"):
		select="SELECT RB_Throttle FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-throttle"):
		select="SELECT Throttle FROM Ships WHERE Owner='%s'"%(str(online_user))		
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-speed"):
		select="SELECT Res_Speed FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-speed-x"):
		select="SELECT Speed_X FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-speed-y"):
		select="SELECT Speed_Y FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-acc"):
		select="SELECT Res_Acc FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-acc-x"):
		select="SELECT Acc_X FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-acc-y"):
		select="SELECT Acc_Y FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-pos-x"):
		select="SELECT Pos_X FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-pos-y"):
		select="SELECT Pos_Y FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-orientation"):
		select="SELECT Orientation FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-ang-speed"):
		select="SELECT Ang_Speed FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="get-ang-acc"):
		select="SELECT Ang_Acc FROM Ships WHERE Owner = '%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		sendm(str(data[0]))

	elif(command=="scan"):
		# getting ship info
		select="SELECT Pos_X,Pos_Y,Scan_Range FROM Ships WHERE Owner='%s'"%(str(online_user))
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		x,y,s_range = int(data[0]),int(data[1]),int(data[2])	
		# getting number of ships
		select = "SELECT count(*) FROM Ships"
		dbcursor.execute(select)
		con.commit()
		data = dbcursor.fetchone()
		nos = int(data[0])
		# finding the ones in range
		inrange = []		
		for i in range(nos):
			select = "SELECT Alias,Owner,Pos_X,Pos_Y FROM Ships WHERE Id=%d and Owner!='%s'"%(i,str(online_user))
			dbcursor.execute(select)
			con.commit()
			data = dbcursor.fetchone()
			if(data!=None):
				alias,owner,posx,posy = data[0],data[1],data[2],data[3]		
				isinrange,distance = inRange(x,y,posx,posy,s_range)			
				if(isinrange):
					li = [str(v) for v in [alias,owner,posx,posy,distance]]
					li = ','.join(li)
					inrange.append(li)
		inrange = '\n'.join(inrange)
		sendm(inrange)			

	elif(command=="exit"):	
		sendm("disconnecting...")
		c.close()		



def inRange(x,y,posx,posy,s_range):
	d=(((float(x-posx))**2)+(float(y-posy)**2))**(1/2)
	ret = False	
	if(d<s_range):
		ret = True	 
	return ret,d
################################################
def sendm(message):
	c.sendto(message.encode(),hp)

def recvm():
	out = c.recv(1024)
	out = out.decode("UTF-8")
	return out

def load_serv():
	global c
	global hp
	global s
	host = 'localhost'
	port = 5001
	hp = (host,port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('',port))
	print("tcp server started")

def ship_own(owner):
	global ships
	global owners
	found = False
	for i in range(len(ob.Ship.ship_list)):
		if(ob.Ship.ship_list[i].owner == owner):
			found = True	
			ships.append(ob.Ship.ship_list[i])
			owners.append(owner)
			print("ships list updated")
	if not(found):
		return None	

def isValid():
	global online_user
	global ships
	global owners
	valid = False
	while not(valid):	
		sendm("user: ")
		user = recvm()
		sendm("pass: ")
		passw = recvm()
		llist = open("userlist").read().split('\n')
		llist = [w for w in llist if w != '']		
		user_pass_list = []
		for i in range(len(llist)):
			u = llist[i].split(',')[0]
			p = llist[i].split(',')[1]
			user_pass_list.append([u,p])		
		for i in range(len(user_pass_list)):
			if(str(user)==user_pass_list[i][0] and str(passw)==user_pass_list[i][1]):
				sendm("hello, "+str(user))
				valid = True
				online_user = str(user)			
		if not(valid):
			sendm("invalid user or password")
	return valid	

def commListen():
	sendm("command: ")	
	data = recvm()
#	if not data:
#		break
	print("received: "+str(data)+'\n')
	isCommand, outp = command(str(data))
	if(isCommand):
		pass#sendm(outp)
	else:
		sendm("invalid command")

def Server():
	global s
	global c
	global hp
	#	
	load_comm_list()
	load_serv()
	load_db()
	#
	s.listen(1)
	c, addr = s.accept()
	print("Connection from: "+str(addr))
	# validation
	if(isValid()):
		# main process	
		while(True):
			commListen()
			sleep(1/30.0)
		c.close()
	else:
		print("error 2324")




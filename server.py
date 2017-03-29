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
	if(command=="set-throttle-ul"):
		pass
	elif(command=="set-throttle-ur"):
		pass
	elif(command=="set-throttle-dl"):
		pass
	elif(command=="set-throttle-dr"):
		pass
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
		pass

	elif(command=="exit"):	
		sendm("disconnecting...")
		c.close()		

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




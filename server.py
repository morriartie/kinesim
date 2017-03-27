#!/usr/bin/python
import os
import sys
import socket
from time import sleep
from random import randint
import oblib as ob
import game as ga

commands = []
ship_by_user = []
online_list = []

ships = []
owners = []

s = None
c = None
hp = None 

# teste
t = ob.Ship("mrrt",1000,10,100)
t.owner = 'moriartie'
# fim teste

def load_users_list():
	global ship_by_user
	ship_by_user = []
	lis = open("userlist").read().split('\n')
	for i in range(len(lis)):
		ship_by_user.append(lis[i].split(','))

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
	s = ships[len(ships)-1]	
	if(command=="status"):
		sendm("orientation: "+str(s.orientation)+'\n')  
		sendm("speed: "+str(s.res_speed)+'\n')
		sendm("acceleration: "+str(s.res_acc)+'\n')
		sendm("pos x: "+str(s.pos_x)+'\n')
		sendm("pos y: "+str(s.pos_y)+'\n')
		sendm("throttle: "+str(s.throttle)+'\n')

	elif(command=="engines"):
		sendm("engines")

	elif(command=="scan"):
		sendm("scan")

	elif(command=="throttle"):
		sendm("throttle: ")
		tr = recvm()
		s.throttle = int(tr)	
		sendm("throttle set to "+str(tr)+'\n')	

	elif(command=="throttle_ul"):
		sendm("ul")

	elif(command=="throttle_ur"):
		sendm("ur")

	elif(command=="throttle_dl"):
		sendm("dl")

	elif(command=="throttle_dr"):
		sendm("dr")

	elif(command=="create ship"):
		sendm("createship")		

	elif(command=="passtime"):
		sendm("passed 1 s"+'\n')
		ob.pass_time(1)

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
	global ships
	global owners
	valid = False
	while not(valid):	
		sendm("user: ")
		user = recvm()
		for i in range(len(ship_by_user)):
			if(str(user)==str(ship_by_user[i][0])):
				#sendm("pass: ")
				sleep(1/30.0)
				sendm("hello "+str(user))	
				sleep(1/30.0)
				valid = True
		if not(valid):
			sendm("invalid user")
	if(valid):
		ship_own(user)
		print("ship l size: "+str(len(ships)))
		print("nome: "+str(ships[len(ships)-1].owner))	
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
	load_users_list()
	load_serv()
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




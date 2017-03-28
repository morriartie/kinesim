#!/usr/bin/python
import os
import sys
import socket
from time import sleep
from random import randint
import oblib as ob
import game as ga
import sqlite3

dbname = "world.db"
database = None
dbcursor = None
con = None

commands = []
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
	if(command=="set-throttle-ul"):
		pass
	elif(command=="set-throttle-ur"):
		pass
	elif(command=="set-throttle-dl"):
		pass
	elif(command=="set-throttle-dr"):
		pass
	elif(command=="set-throttle"):
		pass
	elif(command=="get-throttle-ul"):
		pass
	elif(command=="get-throttle-ur"):
		pass
	elif(command=="get-throttle-dl"):
		pass
	elif(command=="get-throttle-dr"):
		pass
	elif(command=="get-throttle"):
		pass
	elif(command=="get-speed"):
		pass
	elif(command=="get-speed-x"):
		pass
	elif(command=="get-speed-y"):
		pass
	elif(command=="get-acc"):
		pass
	elif(command=="get-acc-x"):
		pass
	elif(command=="get-acc-y"):
		pass
	elif(command=="get-pos-x"):
		pass
	elif(command=="get-pos-y"):
		pass
	elif(command=="get-orientation"):
		pass
	elif(command=="get-ang-speed"):
		pass
	elif(command=="get-ang-acc"):
		pass
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




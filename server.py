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
	if(command=="status"):
		out = "status"
		return out
	elif(command=="engines"):
		out = "engines"
		return out
	elif(command=="scan"):
		out = "scan"
		return out
	elif(command=="throttle"):
		out = "throttle"
		return out
	elif(command=="throttle_ul"):
		out = "ul"
		return out
	elif(command=="throttle_ur"):
		out = "ur"
		return out
	elif(command=="throttle_dl"):
		out = "dl"
		return out
	elif(command=="throttle_dr"):
		out = "dr"
		return out

################################################
def Server():
	load_comm_list()
	load_users_list()
	#
	host = 'localhost'
	port = 5001
	hp = (host,port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('',port))
	print("tcp server started")
	s.listen(1)
	c, addr = s.accept()
	print("Connection from: "+str(addr))
	# validation
	denied = True
	while(denied):	
		c.sendto("user: ".encode(),hp)
		user = c.recv(1024)
		user = user.decode("UTF-8")
		for i in range(len(ship_by_user)):
			if(str(user)==str(ship_by_user[i][0])):
				c.sendto(("hello "+str(user)).encode(),hp)	
				denied = False
		if(denied):
			c.sendto(("invalid user").encode(),hp)
	# main process	
	while True:
		c.sendto(("command: ").encode(),hp)	
		data = c.recv(1024)
		if not data:
			break
		data = data.decode("UTF-8")
		print("received: "+str(data)+'\n')
		isCommand, outp = command(str(data))
		if(isCommand):
			c.sendto(outp.encode(),hp)
		else:
			c.sendto(("invalid command").encode(),hp)
	c.close()





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
s = None
c = None
hp = None 

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
	denied = True
	while(denied):	
		sendm("user: ")
		user = recvm()
		for i in range(len(ship_by_user)):
			if(str(user)==str(ship_by_user[i][0])):
				sendm("hello "+str(user))	
				denied = False
		if(denied):
			sendm("invalid user")
	# main process	
	while True:
		sendm("command: ")	
		data = recvm()
		if not data:
			break
		print("received: "+str(data)+'\n')
		isCommand, outp = command(str(data))
		if(isCommand):
			sendm(outp)
		else:
			sendm("invalid command")
	c.close()





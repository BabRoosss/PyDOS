from os import system

def clear():
	system('clear')
def nano():
	system('nano')
def ls():
	system('ls')
def pwd():
	system('pwd')
def cd():
	system('cd')
def cdDown():
	system('cd ..')
def update():
	system('git clone https://github.com/BabRoosss/PyDOS')
def updateDirectory():
	system('cd ~')
clear()

print('=========================PyDOS=========================')
while 1==1:
	print()
	command = input('>')

	if command == 'clear':
		print('=========================PyDOS=========================')
		clear()
	if command == 'logout':
		clear()
		print('You have been loged out of your session.')
		print('Please log in to continue using PyDOS!')
		exec(open('PyDOS_Login.py').read())
	if command == 'nano':
		nano()
	if command == 'sysinfo':
		print('Writen in Python 3')
		print('Made by Bab Roosss')
	if command == 'exit':
		break
	if command == 'ls':
		print()
		ls()
	if command == 'pwd':
		pwd()
	if command == 'help':
		print('Help	Prints help info')
		print('Clear	Clears the screen')
		print('Nano	Opens a TextEditor')
		print('ls	Prints the contents of the current directory')
		print('pwd	Prints current working directory')
		print('sysinfo	Prints info about the shell')
		print('exit	. . . exit')
	if command == 'cd':
		$command

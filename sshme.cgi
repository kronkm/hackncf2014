#!C:/Python34/python

# Import modules for CGI handling
import cgi, cgitb

# Import other modules for execution via command line (?)
import subprocess
import sys
import os

# Import paramiko, which will handle ssh gracefully
import paramiko

# Setup the HTML DOCTYPE and framework
print ("Content-type: text/html\n\n")
print ("<html>")
print ("<head><link rel='stylesheet' type='text/css' href='/css/simpleGrid/simplegrid.css'><title>RAPTOR Interface</title></head>")
print ("<center>Welcome to RAPTORsphere</center>")
print ("<body>")
print ("<br></br>")

# Create list object which RAPTOR output can be placed into
myList = []

# Setup ssh into a RAPTOR, capture output of appliance all command
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('192.168.1.146', username='hackathon', 
    password='hackathon')
stdin, stdout, stderr = ssh.exec_command("cd /opt/Raptor; sudo python3 raptor.py appliance 0 all")
stdin.flush()

counter = 0

print ("<center>")
# Capture output from appliance all command
for line in stdout:

	#Setup css that will have to be printed to setup grid, depending on which position the current light will be in (0-2)
	if counter == 0:
		firstHalf = "<div class=grid grid-pad><div class=col-1-3><div class=content>"
		secondHalf = "</div></div>"
	elif counter == 1:
		firstHalf = "<div class=col-1-3><div class=content>"
		secondHalf = "</div></div>"
	else:
		firstHalf = "<div class=col-1-3><div class=content>"
		secondHalf = "</div></div></div>"
		
	print(firstHalf)
	tempList = line.split(",")
	if tempList[2] == 'Teal':
		print ("<img src=/images/teal.png>")
	elif tempList[2] == 'Green':
		print ("<img src=/images/green.png>")
	elif tempList[2] == 'Blue':
		print ("<img src=/images/blue.png>")
	elif tempList[2] == 'Purple':
		print ("<img src=/images/purple.png>")
	elif tempList[2] == 'Red':
		print ("<img src=/images/red.png>")
	elif tempList[2] == ' ':
		print ("<img src=/images/off.png>")
	else:
		print("<br>No image</br>")
	
	
	print ("<p>" + tempList[0] + "</p>")
	print (secondHalf)
	counter = counter + 1
	if counter == 3:
		counter = 0
print("</center>")
print ("</body>")
print ("</html>")

#!/usr/bin/python

import sys
import time
import logging

# logging.basicConfig(filename='calculator1.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')
logging.basicConfig(filename='cal.log',
	level=logging.INFO,
	format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')
def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def multiply(g,h):
	return g*h

def divide(y,t):
	return y/t



name= raw_input("Hello, Please tell me your name\nEnd to exit")
logging.info("Welcome",name)
if name=="End" or name=="end":
   print ("The program is exiting")
   sys.exit()
	
else:
	print "Welcome",name
	logging.info("Welcome")



cont = "y"
while cont == "y" or cont == "Y":

	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")

	choice= input("Enter choice 1/2/3/4:")
    

	num1= input("Enter First Number:")

	time.sleep(1)
	num2= input("Enter Second Number:")
	logging.info("Input has been taken")
	if choice ==1:
		print "Choice1"
	
		print(num1,"+",num2,"=", add(num1,num2))
	elif choice ==2:
		a=num1,"-",num2,"=", subtract(num1,num2)
		print "Congratulations, The answer is:",a
	elif choice ==3:
		print (num1,"*",num2,"=",multiply(num1,num2))
	elif choice ==4:
		print (num1,"*",num2,"=",divide(num1,num2))
	else:
		print("Invalid Option")		
	
	print name	
	cont = raw_input("Do you want to Continue?y/n:")

print("Thankyou for choosing us. THe program has ended")
logging.info("The program has finished")



										# Logging practice 
# import logging
# logging.basicConfig(filename='sam1.log',
# 	level=logging.INFO,
# 	format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')

# try:
# 	logger = logging.getLogger(__name__)

# 	logger.info('Start reading database')
# 	# read database here
# 	records = {'john': 55, 'tom': 66}
# 	a=raw_input()
# 	logger.debug('Records: %s', records)
# 	logger.info('Updating records ...')
# 	# update records here
# 	logger.info('Finish updating records')

# except KeyboardInterrupt:
# 	# logger.error("Failed to run script", exc_info=True)
#     print('\n\nKeyboard exception received. Exiting.')
#     logging.error("Keyboard exception received. Exiting.")
#     exit()
# else:
# 	logging.info("THe script has run perfectly:")



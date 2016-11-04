#!/bin/python

# h2d
# A simple hex-dec converter in python for shell
# Takes a single hex value for input and outputs the decimal equivalent

#	Author:		D. Scott Boggs
import sys
values={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}	#decimal to hex values
dec=0
def main():
	if len(sys.argv)==2:		#check for a single input value
		dec=h2d(sys.argv[1])	# and call the conversion procedure, saving the result to an int value
	else:						#and exit with error if ther isn't one or if there are more than one arguments passed
		error("Invalid input - " + str(len(sys.argv)) + " is too many or too few arguments")
	print dec		# finally, print the value

def h2d(hexIn):		#the conversion algorithm
	decOut=0		# output variable
	decArray=[]		#array to hold each individual digit
	place=0			#takes note of the place (hundreds, tens, ones, etc.)
	for s in list(hexIn):		# iterates through each hex digit
		try:					#checks to make sure the digit is a valid hex number
			decArray.append(values[s])	# and appends its decimal equivalent to decArray
		except KeyError:		# if it's not a valid hex digit
			error(s + " is not a valid hex digit")	# exits with an error message that says so
		place+=1				# and takes note of how many places there are
	for i in decArray:		#iterates through the array of decimal values
		place-=1			# from highest place to lowest
		decOut+=i*(16**place)	#and adds the current place value to the decimal value
	return decOut		#then returns the result
def error(s):
	print("Error: " + s)		#error message
	exit(1)
main()

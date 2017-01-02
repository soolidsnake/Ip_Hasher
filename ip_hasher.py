"""

Author : BITAM Salim

"""

import os.path
from random import randint


def ip_generator(fname, n):

	fd = open(fname, 'w')

	
	i = 0
	while(i < n):
		ip = str(randint(0,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255)) + '.' + str(randint(0,255))
		fd.write(ip + '\n')
		i +=1
	fd.close()

# Hash function
def hash_function(ip):

	ip = ip.split('.')
	hashed_value = int(ip[0]) + int(ip[1]) + ((int(ip[2]) * int(ip[3]))/3) % 9490
	return(hashed_value)

def ip_class(ip):


	ip = ip.split('.')

	if(int(ip[0]) >= 0 and int(ip[0]) <= 127):
		return(0)

	elif(int(ip[0]) >= 128 and int(ip[0]) <= 191):
		return(1)

	elif(int(ip[0]) >= 192 and int(ip[0]) <= 223):
		return(2)

	elif(int(ip[0]) >= 224 and int(ip[0]) <= 239):
		return(3)

	elif(int(ip[0]) >= 240 and int(ip[0]) <= 255):
		return(4)

def load_function(fname, list_A, list_B, list_C, list_D, list_E):

	cpt = 0

	with open(fname, 'r') as fd:
		for line in fd:
			line = line.strip()
			ip = line.split('.')

			hashed = int(hash_function(line))

			if(ip_class(line) == 0):
				if(len(list_A[hashed]) > 0):
					cpt += 1
				list_A[hashed].append(line)

			elif(ip_class(line) == 1):
				if(len(list_B[hashed]) > 0):
					cpt += 1
				list_B[hashed].append(line)

			elif(ip_class(line) == 2):
				if(len(list_C[hashed]) > 0):
					cpt += 1
				list_C[hashed].append(line)

			elif(ip_class(line) == 3):
				if(len(list_D[hashed]) > 0):
					cpt += 1
				list_D[hashed].append(line)

			elif(ip_class(line) == 4):
				if(len(list_E[hashed]) > 0):
					cpt += 1
				list_E[hashed].append(line)

	print ("Collision counter : ", cpt)

#Check function
def check_function(list_A, list_B, list_C, list_D, list_E, req):

	hashed = int(hash_function(req))

	l=[]

	if(ip_class(req) == 0):
		l = list_A


	elif(ip_class(req) == 1):
		l = list_B

	elif(ip_class(req) == 2):
		l = list_C

	elif(ip_class(req) == 3):
		l = list_D

	elif(ip_class(req) == 4):
		l = list_E
	
	i = 0

	while(i < len(l[hashed])):
		if(req == l[hashed][i]):
			return("found")
			break

		i += 1
	return("not found")


# Main function
def main():
	
	fname = 'ip_container'

	list_A =[]
	list_B =[]
	list_C =[]
	list_D =[]
	list_E =[]

	#Makes the lists as if they were static arays
	for i in range(0,10000):
		list_A.append([])
		list_B.append([])
		list_C.append([])
		list_D.append([])
		list_E.append([])

	print("\t\tWelcome to ip_hasher\n")

	if(os.path.isfile(fname) == False ):
		print("I will generate first a list of ip addresses for you")
		while(True):
			try:
				n = int(input("Enter how much IPs you want to generate : "))
			except ValueError:
				print("Error inter a correct integer")
				continue
			break
		ip_generator(fname, n)
	load_function(fname, list_A, list_B, list_C, list_D, list_E)

	while(True):

		req = input("\n[+] Enter an ip address to check if it exist \n[+] 'l' to list the ips contained in the file \n[+] 'q' to exit \n ")
		req = req.strip()
		if(req == 'q'):
			break

		if(req == 'l'):
			with open(fname, 'r') as fd:
				for line in fd:
					print(line)

			continue

		print(check_function(list_A, list_B, list_C, list_D, list_E, req))






if __name__ == '__main__':
	main()
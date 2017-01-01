"""

Author : BITAM Salim

"""

import os.path
from random import randint


def ip_generator(fname):

	fd = open(fname, 'w')
	while(True):
		try:
			n = int(input("Enter how much IPs you want to generate : "))
		except ValueError:
			print("Error inter a correct integer")
			continue
		break
	
	i = 0
	while(i < n):
		ip = str(randint(1,254)) + '.' + str(randint(1,254)) + '.' + str(randint(1,254)) + '.' + str(randint(1,254))
		fd.write(ip + '\n')
		i +=1
	fd.close()




#Main function
def main():
	
	fname = 'ip_container'


	print("\t\tWelcome to ip_hasher")

	if(os.path.isfile(fname) == False ):
		print("I will generate first a list of ip addresses for you")
		ip_generator(fname)

	







if __name__ == '__main__':
	main()
import sys

if __name__ == "__main__": 

	if(float(int(sys.argv[1]) - int(sys.argv[3])/2) <= int(int(sys.argv[4])) <= float(int(sys.argv[1]) + int(sys.argv[3])/2) and float(int(sys.argv[2]) - int(sys.argv[3])/2) <= int(int(sys.argv[5])) <= float(int(sys.argv[2]) + int(sys.argv[3])/2)):
		print("it is there")
	else: 
		print("it is not there")
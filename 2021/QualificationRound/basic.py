import sys

def read_file(file):
	stdin_fileno = sys.stdin
	sys.stdin = open(file,'r')
	ip = []
	
	for line in sys.stdin:
		ip.append(line)

	sys.stdin.close()
	sys.stdin = stdin_fileno
	return ip

def write_file(file, op):
	stdout_fileno = sys.stdout
	sys.stdout = open(file,'w')
	
	for c in range(0, len(op)):
		sys.stdout.write(op[c])
		if not c == len(op) - 1:
			sys.stdout.write('\n')

	sys.stdout.close()
	sys.stdout = stdout_fileno

def main():
	pass


if __name__ == "__main__":
	main()

import sys

def read_file():
	stdin_fileno = sys.stdin
	ip = []

	sys.stdin = open('','r')
	for line in sys.stdin:
		ip.append(line)

	sys.stdin.close()
	sys.stdin = stdin_fileno
	return ip

def write_file(op):
	stout_fileno = sys.stdout

	sys.stdout = open('','r')
	for line in op:
		sys.stdout.write(op + '\n')

	sys.stdout.close()
	sys.stdout = stdout_fileno

def main():
	pass


if __name__ == "__main__":
	main()

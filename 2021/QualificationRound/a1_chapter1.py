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
	
	for line in op:
		sys.stdout.write(line + '\n')

	sys.stdout.close()
	sys.stdout = stdout_fileno

def test_vow(l):
	if l in ['A','E','I','O','U']:
		return True
	return False

def get_max(s):
	seconds = []
	test_char = s
	test_char += 'AB'

	for e in test_char:
		counter = 0
		for l in s:
			if not l == e:
				if test_vow(l) == test_vow(e):
					counter += 2
				else:
					counter += 1
		seconds.append(counter)

	return min(seconds)

def main():
	ip = read_file('./Input/consistency_chapter_1_input.txt')
	num = int(ip.pop(0))
	op = []

	for c in range(0, num):
		op.append(f"Case #{c+1}: {get_max(ip[c].strip())}")

	write_file('./Output/consistency_chapter_1_output.txt', op)
		

if __name__ == "__main__":
	main()
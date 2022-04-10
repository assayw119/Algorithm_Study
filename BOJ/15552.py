import sys

a = int(sys.stdin.readline().rstrip())

for i in range(a):
        b, c = sys.stdin.readline().strip().split()
        print(int(b) + int(c))
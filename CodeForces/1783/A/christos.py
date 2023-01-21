import sys
input = sys.stdin.readline
def inp(): #int input
    return(int(input()))
def inlt(): #int list input
    return(list(map(int,input().split())))
def insr(): #string input (list of chars)
    s = input()
    return(list(s[:len(s) - 1]))
def invr(): #space separated ints
    return(map(int,input().split()))
 
t = inp()
for _ in range(t):
	n = inp()
	a = inlt()
	mn, mx = min(a), max(a)
	if mn == mx:
		print('NO')
	else:
		print('YES')
		a.remove(mn)
		a.remove(mx)
		a = [mx, mn] + a
		print(*a)
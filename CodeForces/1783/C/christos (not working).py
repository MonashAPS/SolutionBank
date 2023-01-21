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
	n, m = invr()
	a = inlt()
	
	#just some preprocessing for keeping track of indices (idk if this is needed)
	for i in range(n):
		a[i] = (a[i], i)
		
	#sorted version of a
	a2 = sorted(a, key = lambda x : x[0])
	
	#prefix sum which will help find the max number of games we can win
	ps = [a2[0][0]]
	for i in range(1, n):
		ps += [ps[-1] + a2[i][0]]
	
	#prefix sum[i] = sum of elements from 0 to i
	#can be calculated by keeping track of the prefix sum of the last index
	#and just adding the current index's value to it
	
	
	
	#finding maxwins, and the amount of total time spent (so we can deduce how much
	#extra time we have to possibly win against a higher level player instead)
	maxwins = 0
	timespent = 0
	for i in range(n):
		#max number of wins we can get = largest a[i] <= m
		if ps[i] <= m:
			maxwins = i + 1
			timespent = ps[i]
		else:
			break
	
	#we've won against the first maxwins players in the sorted a2
	#so from index maxwins onwards, that player beats us
	
	for i in range(n):
		a2[i] = (a2[i][0], a2[i][1], i) #this is so cringe lol
		
	a2.sort(key = lambda x : x[1]) #sort back to original order
	
 
	#print(ps)
	
	winsagainstplayer = [a2[i][2] >= maxwins for i in range(n)]
 
	
	#the number of wins each player has assuming you prepare for all the easiest players
	#= the number they win automatically  = i
	#+ 1 if they beat you
	
	wins = [i + winsagainstplayer[i] for i in range(n)]
 
	#print('a', maxwins)
	
	#where is the player in this ranking?
	
	#actual ranking = n - i
	
	rankingindex = -1
	for i in range(n):
		if wins[i] > maxwins:
			break	
		rankingindex = i
		
	#print('a', rankingindex)
	
	#print('a', rankingindex, winsagainstplayer)
	if rankingindex != n - 1 and (winsagainstplayer[rankingindex + 1]):
		sparetime = m - timespent
		
		#best opportunity is finding the least skilled player we win against
		
		#least skilled player that we win against
		lsp = 0
		if maxwins != 0:
			lsp = float('inf')
			for c in a:
				if c[0] < lsp and not (winsagainstplayer[c[1]]):
					lsp = c[0]
		
		
		diff = a[rankingindex + 1][0] - lsp
		#print(sparetime, diff)
		#print(diff, sparetime)
		if diff <= sparetime:
			#rankingindex + 1 loses a win
			#we gain a win
			maxwins += 1
			for i in range(rankingindex + 1, n):
				if wins[i] > maxwins:
					break
				rankingindex = i
	ranking = n - rankingindex
	
	print(ranking)

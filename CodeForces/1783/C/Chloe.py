testcases = int(input())
for _ in range(testcases):
    # get input
    n, m = map(int, input().split())
    prep = list(map(int, input().split()))
    sorted_prep = sorted(prep)
    
    # initialise variables and figure out if 1+ wins can be achieved
    ps = [0] # prefix sum of preps
    max_wins = n # max wins
    # iterate through sorted_prep until sum_prep > m to find max_wins
    for i, num in enumerate(sorted_prep):
        ps.append(ps[i] + num)
        if ps[-1] > m: # don't need to get the prefix sum past max_wins-1
            max_wins = i
            break
    
    # check to see if prep[max_wins] can be won against without reducing win count
    if max_wins == n: # win against all
        print(1)
    else: # you might be able to win against prep[max_wins]
        # min_prep is the minimum preparation time required to achieve max_wins-1 wins
        min_prep = ps[max_wins-1]
        if min_prep + prep[max_wins] <= m: #you can win against prep[max_wins]
            print(n-max_wins)
        else: # you can't win against prep[max_wins] without reducing win count
            print(n+1-max_wins)

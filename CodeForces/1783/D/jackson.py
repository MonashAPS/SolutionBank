# MAPS
# Written by Jackson and Comments from Christos.
# Current Result: TLE because Python but is the intended solution.
# Also attempted with dict/defaultdict.

import sys
sys.setrecursionlimit(10000)
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

MAX_VAL = 300
MAX_N = 300
MAX_A = MAX_VAL * MAX_N

MOD = 998244353

DP = [
    [None for _ in range(-MAX_A, MAX_A+1)]
    for _ in range(MAX_N+1)
]

def solve(case):
    n = inp()
    a_vals = inlt()
    return dp_solve(a_vals, (0, a_vals[1]))

def dp_solve(a_vals, key):
    i, k = key
    if DP[i][k] != None:
        return DP[i][k]
    if i == len(a_vals)-2:
        # Only 2 values left, no action.
        return 1
    # Now, complete the action with index 1 (value k)
    if k == 0:
        DP[i][k] = dp_solve(a_vals, (i+1, a_vals[i+2]))
    else:
        DP[i][k] = (
            dp_solve(a_vals, (i+1, a_vals[i+2]+k))
            + dp_solve(a_vals, (i+1, a_vals[i+2]-k))
        ) % MOD
    return DP[i][k]

# DP[i][k] = Splice from i to end, with second value k
# [1, 2, 3, 4, 5], i=2, k=4, # [1, 4, 5]

# [1, 2, 3, 4, 5] # i = 0, k = 2
# -> [2, 1, 4, 5] # i = 1, k = 1
# -> [2, 5, 4, 5] # i = 1, k = 5

print(solve(0))


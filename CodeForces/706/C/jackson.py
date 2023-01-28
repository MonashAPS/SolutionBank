# MAPS
# Written by Jackson, with comments + debugging by Chloe.
# Current Result: AC

import sys
sys.setrecursionlimit(10000)
# Removed the `input` line to avoid newline issues
def inp(): #int input
    return(int(input()))
def inlt(): #int list input
    return(list(map(int,input().split())))
def insr(): #string input (list of chars)
    s = input()
    return(list(s[:len(s) - 1]))
def invr(): #space separated ints
    return(map(int,input().split()))

n = inp()
energies = inlt()
strings = [input() for _ in range(n)]

def compare(s1, b, s2, f):
    # There are more efficient ways to do this / precompute it with DP but this is fine.
    if b:
        s1 = s1[::-1]
    if f:
        s2 = s2[::-1]
    return s1 <= s2

DP = {}
def points(b, x):
    # Compute the cost for the previous flip
    flip = energies[x-1] if b else 0
    if x == n:
        return flip
    if (b, x) in DP:
        return DP[(b, x)]
    best = float("inf")
    for f in range(2):
        # Either we do / don't flip strings[x]
        if compare(strings[x-1], b, strings[x], f):
            best = min(best, flip + points(f, x+1))
    DP[(b, x)] = best
    return best

# Pre-computation step to avoid Recursion Limit issues. Bottom up.
for x in range(n, 0, -1):
    for b in range(2):
        points(b, x)

def solve():
    best = float("inf")
    for f in range(2):
        best = min(best, points(f, 1))
    return best if best != float("inf") else -1

print(solve())

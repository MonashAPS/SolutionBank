# MAPS
# Written by __, __ and __.
# Current Result: AC/WA/TLE
# Further Comments

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

def solve(case):
    pass

t = inp()
for case in range(t):
    print(solve(case))

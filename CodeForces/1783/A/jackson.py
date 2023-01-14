# MAPS
# Written by __, __ and __.
# Current Result: AC
# Inspired by Cros' Solution, but still sorts it to keep things simple.

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
    _ = inp()
    nums = inlt()
    # Sorting by nums decreasing ensures almost all cases are dealt with
    nums.sort(reverse=True)
    if nums[0] == nums[-1]:
        return "NO"
    else:
        # Swap the second largest and minimum elements.
        # This ensures that index [1] is smaller than [0]
        # And since the maximum is at the front (and [1] is non-zero) everything after this is less.
        nums[1], nums[-1] = nums[-1], nums[1]
        return "YES\n"+" ".join(map(str, nums))

t = inp()
for case in range(t):
    print(solve(case))

import math
import sys
input = sys.stdin.readline

max_i = 1000000
arr = [0] * (max_i + 5)
tree = [0] * (1 << (math.ceil(math.log2(max_i)) + 1))

def find(nd, st, e, c):
    if st == e: return st
    
    mid = int((st + e) / 2)
    if tree[nd * 2] >= c: return find(nd * 2, st, mid, c)
    return find(nd * 2 + 1, mid + 1, e, c - tree[nd * 2])

def update(nd, st, e, idx, diff):
    if idx < st or idx > e : return
    tree[nd] = tree[nd] + diff
    
    if st != e:
        mid = int((st + e) / 2)
        update(nd * 2, st, mid, idx, diff)
        update(nd * 2 + 1, mid + 1, e, idx, diff)
        
N = int(input())

while N:
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        idx = inp[1]
        pos = find(1, 1, max_i, idx)
        print(pos)
        arr[pos] -= 1
        update(1, 1, max_i, pos, -1)
    else:
        idx = inp[1]
        val = inp[2]
        arr[idx] += val
        update(1,1,max_i,idx,val)
    N -= 1
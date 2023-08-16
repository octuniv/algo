import sys
input = sys.stdin.readline

N, M = map(int, input().split())
word_list= dict()
cnt = 0
while N > 0:
    N -= 1
    word = input().strip()
    if len(word) < M: continue
    if word not in word_list:
        word_list[word] = 1
    else:
        word_list[word] += 1

rev_ref = dict()
for k, v in word_list.items():
    if v not in rev_ref:
        rev_ref[v] = [k]
    else:
        rev_ref[v].append(k)
    
keys = sorted([k for k in rev_ref.keys()], reverse=True)
ans = []
for k in keys:
    ans.extend(sorted(rev_ref[k], key = lambda x: (-len(x), x)))
    
for a in ans:
    print(a)
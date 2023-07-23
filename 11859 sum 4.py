import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [0, ]
num_list.extend(list(map(int, input().split())))

acc_list = []
for _ in range(M):
    acc_list.append(tuple(map(int, input().split())))
    
acc_array = [0, ]

for i in range(1, N + 1):
    acc_array.append(num_list[i] + acc_array[i - 1])
    
for s, e in acc_list:
    print(acc_array[e] - acc_array[s - 1])
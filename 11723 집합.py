import sys
input = sys.stdin.readline

arr = [0] * 21

def add(x):
    arr[x] = 1
    return

def remove(x):
    arr[x] = 0
    return

def check(x):
    print(arr[x])
    return

def toggle(x):
    if arr[x] == 1:
        arr[x] = 0
    else:
        arr[x] = 1
    return

def all():
    for i in range(1,21):
        arr[i] = 1
    return

def empty():
    for i in range(1,21):
        arr[i] = 0
    return

exec_func = dict()
exec_func["add"] = add
exec_func["remove"] = remove
exec_func["check"] = check
exec_func["toggle"] = toggle
exec_func["all"] = all
exec_func["empty"] = empty

N = int(input())

for _ in range(N):
    in_val = list(map(str, input().split()))
    if len(in_val) > 1:
        exec_func[in_val[0]](int(in_val[1]))
    else:
        exec_func[in_val[0]]()
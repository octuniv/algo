import sys
input = sys.stdin.readline

numbers = [
    [2, 2, 2, 1, 2, 2, 2],
    [1, 1, 2, 1, 1, 2, 1],
    [2, 1, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 1, 2, 2],
    [1, 2, 2, 2, 1, 2, 1],
    [2, 2, 1, 2, 1, 2, 2],
    [2, 2, 1, 2, 2, 2, 2],
    [2, 1, 2, 1, 1, 2, 1],
    [2 for _ in range(7)],
    [2, 2, 2, 2, 1, 2, 2]
]
diff = [[sum([1 if numbers[i][e] != numbers[j][e] else 0 for e in range(7)]) for j in range(10)] for i in range(10)]
N, K, P, X = map(int, input().split())
st = 1
ans = -1
pX = []
while X > 0:
    pX.append(X % 10)
    X //= 10
while K > len(pX):
    pX.append(0)

while st <= N:
    pC = []
    tst = st
    while tst > 0:
        pC.append(tst % 10)
        tst //= 10
    while K > len(pC):
        pC.append(0)
    diff_i = 0
    for i in range(K):
        diff_i += diff[pC[i]][pX[i]]
    if diff_i <= P:
        ans += 1
    st += 1
print(ans)
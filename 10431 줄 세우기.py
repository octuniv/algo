import sys
import bisect
input = sys.stdin.readline

P = int(input())
ans_list = []

while P:
    P -= 1
    stu = list(map(int, input().split()))
    T = stu[:1]
    stu = stu[1:]
    ans, cnt = 0, 1
    line = [stu[0]]
    while cnt < 20:
        a = bisect.bisect_left(line, stu[cnt])
        if a == cnt:
            line.append(stu[cnt])
        else:
            line.insert(a, stu[cnt])
            ans += cnt - a
        cnt += 1
    ans_list.append(ans)
for i in range(len(ans_list)):
    print("{} {}".format(i + 1, ans_list[i]))
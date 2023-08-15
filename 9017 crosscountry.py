import sys
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    N = int(input())
    cc = list(map(int, input().split()))
    M = -1
    for c in cc:
        M = max(M, c)
    team = [[] for _ in range(M + 1)]
    for i in range(len(cc)):
        team[cc[i]].append(i + 1)
    avail_team = [True if len(t) == 6 else False for t in team]
    team = [[] for _ in range(M + 1)]
    count = 1
    for c in cc:
        if avail_team[c]:
            team[c].append(count)
            count += 1
    ans = -1
    m_count = 2000000
    for i in range(len(team)):
        if avail_team[i]:
            tp = sum(team[i][:4])
            if m_count > tp:
                ans = i
                m_count = tp
            elif m_count == tp and team[i][4] < team[ans][4]:
                ans = i
    print(ans)
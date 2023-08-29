import sys
input = sys.stdin.readline

p, m = map(int, input().split())

rooms = list()
lobby = list()
idx = -1

for _ in range(p):
    level, nick = input().split()
    level = int(level)
    if not lobby:
        rooms.append([[level, nick]])
        idx += 1
        if m != 1:
            lobby.append(idx)
    else:
        l_idx = -1
        for t_idx in range(len(lobby)):
            l_b = rooms[lobby[t_idx]][0][0]
            if not (level > l_b + 10 or level < l_b - 10):
                l_idx = t_idx
                break
        if l_idx == -1:
            rooms.append([[level, nick]])
            idx += 1
            if m != 1:
                lobby.append(idx)
        else:
            r_idx = lobby[l_idx]
            rooms[r_idx].append([level, nick])
            if len(rooms[r_idx]) >= m:
                lobby.pop(l_idx)
                
for idx in range(len(rooms)):
    rooms[idx].sort(key=lambda x: x[1])
    if len(rooms[idx]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for player in rooms[idx]:
        print(f'{player[0]} {player[1]}')
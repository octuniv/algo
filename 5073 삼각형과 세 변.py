import sys
input = sys.stdin.readline

while True:
    l = sorted(list(map(int, input().split())))
    if l[0] == 0 and l[1] == 0 and l[2] == 0 : break
    if l[0] == 0 or l[0] + l[1] <= l[2]: 
        print("Invalid")
        continue
    condf = l[0] == l[1]
    condc = l[1] == l[2]
    if condf and condc: print("Equilateral")
    elif condf or condc: print("Isosceles")
    else: print("Scalene")
import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']
ec = ['e', 'o']
while True:
    pw = input().strip()
    if pw == "end":
        break
    is_vowel = False
    not_acc = True
    not_st = True
    p_c, a_c, a_st = -1, 1, 0
    for c in pw:
        if not is_vowel and c in vowels:
            is_vowel = True
        if (p_c not in vowels and c in vowels) or (p_c in vowels and c not in vowels):
            a_st = 1
        else:
            a_st += 1
            if a_st >= 3:
                not_st = False
                break
        if p_c != c:
            p_c = c
            a_c = 1
        else:
            if c in ec and a_c == 1:
                a_c += 1
            else:
                not_acc = False
                break
    if not_acc and is_vowel and not_st:
        print("<{}> is acceptable.".format(pw))
    else:
        print("<{}> is not acceptable.".format(pw))
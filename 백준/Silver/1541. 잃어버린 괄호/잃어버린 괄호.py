s = input()

if '-' not in s:
    s = s.split('+')
    a = []
    for i in range(len(s)):
        a.append(int(s[i]))
    print(sum(a))
else:
    s = s.split('-')
    for i in range(len(s)):
        if '+' in str(s[i]):
            a = s[i].split('+')
            b = []
            for j in a:
                b.append(int(j))
            
            s[i] = sum(b)
    su = int(s[0])
    for i in range(1, len(s)):
        su -= int(s[i])
    print(su)
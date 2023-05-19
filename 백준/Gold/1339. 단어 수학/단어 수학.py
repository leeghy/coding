N = int(input())
words = []
for i in range(N):
    words.append(input())
dic = {}
for word in words:
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 10**(len(word)-i-1)
        elif word[i] in dic:
            dic[word[i]] += 10**(len(word)-i-1)

sort_dic = dict(sorted(dic.items(), reverse=True, key=lambda x:x[1]))
num = 9
num_dic = {}
for i in sort_dic:
    num_dic[i] = num
    num -= 1
calc = 0
for i in words:
    s = ''
    for j in i:
        s += str(num_dic[j])
    calc += int(s)
print(calc)

T = int(input(''))
w = []
if 1 <= T <= 1000000:
    for i in range(T):
        words = input('')
        if 1 <= len(words) <= 100:
            w.append(words)

for word in w:
    i = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i = i - 1
    if i == 0:
        print('no answer')
    else:
        j = len(word) - 1
        while word[j] <= word[i - 1]:
            j = j - 1
        l = list(word)
        l[i - 1], l[j] = word[j], word[i - 1]
        l[i:] = l[len(word) - 1:i - 1:-1]
        word = ''.join(l)
        print(word)


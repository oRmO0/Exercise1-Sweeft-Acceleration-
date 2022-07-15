from collections import Counter
n = int(input(" \n"))
word_list = []
if 1 <= n <= 1000000:
    for i in range(n):
        word = input(" \n").lower()
        word_list.append(word)
word_list_set = set(word_list)
print(len(word_list_set))
for i in Counter(word_list).values():
    print(i, end=' ')

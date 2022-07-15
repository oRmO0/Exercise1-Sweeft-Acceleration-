r, c, n = input().split()
r, c, n = int(r), int(c), int(n)
initial_state = []
for i in range(r):
    row = list(input())
    initial_state.append(row)


def explosion(initial_state, r, c):
    grid = [['O' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if initial_state[i][j] == 'O':
                grid[i][j] = '.'
                if i + 1 < r:
                    grid[i + 1][j] = '.'
                if i > 0:
                    grid[i - 1][j] = '.'
                if j + 1 < c:
                    grid[i][j + 1] = '.'
                if j > 0:
                    grid[i][j - 1] = '.'
    return grid


"""

0 - Initial State
1 - Initial State
2 - Full State
3 - Detonatet State
4 - Full State
5 - Initial State
6 - Full State
7 - Detonated State
8 - Full State
9 - Initial State
10 - Full State

Initial State - 0,1,5,9,13,17,21,24
Full State - 2,4,6,8,10,12,14,16,18,20
Detonated State - 3,7,11,15,19,23,27

Initial State
n == 0 or n == 1 or (n - 1) % 4 == 0

Detonated State
(n + 1) % 4 == 0

Full State
n % 2 == 0
"""

if n % 2 == 0 and n != 0:
    full_state = [['O' for i in range(c)] for j in range(r)]
    for i in range(r):
        print(''.join(map(str, full_state[i])))
else:
    detonated_state = explosion(initial_state, r, c)
    if n == 1 or n == 0 or (n - 1) % 4 == 0:
        for i in range(r):
            print(''.join(map(str, initial_state[i])))
    elif (n + 1) % 4 == 0:
        for i in range(r):
            print(''.join(map(str, detonated_state[i])))

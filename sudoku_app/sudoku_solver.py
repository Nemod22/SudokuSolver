def valid_options(t, i, j):
    """Returns a set of all valid options for cell t[i][j]"""
    if t[i][j] != 0: return set()

    s = set(range(1,10))

    s -= {t[x][j] for x in range(9)}
    s -= {t[i][x] for x in range(9)}

    box_y = i//3
    box_x = j//3
    s -= {t[i][j] for i in range(box_y*3, box_y*3+3)
                  for j in range(box_x*3, box_x*3+3)}
    return s

def is_valid_board(t):
    
    def distinct(l):
        """checks if any number (excluding zero), is in list more than once"""
        for i in l:
            if i != 0:
                if l.count(i) > 1:
                    return False
        return True
    
    for row in t:
        if not distinct(row): return False
    
    for column in [[t[i][j] for i in range(9)] for j in range(9)]:
        if not distinct(column): return False

    for box_x in range(3):
        for box_y in range(3):
            if not distinct([t[i][j] for i in range(box_y*3, box_y*3+3) for j in range(box_x*3, box_x*3+3)]):
                return False

    
    return True


def solve(t):
    print('Solving started')

    if not is_valid_board(t):
        print('Not valid board')
        return False
    
    def backtrack(p):
        if len(p) == 0:
            return True
        else:
            k = 0
            s = valid_options(t, p[0][0], p[0][1])
            for m in range(1, len(p)):
                r = valid_options(t, p[m][0], p[m][1])
                if len(r) < len(s):
                    s, k = r, m
            
            i, j = p.pop(k)
            for n in valid_options(t, i, j):
                t[i][j] = n
                if backtrack(p):
                    return True
                t[i][j] = 0
            p.append((i, j))
            return False

    if backtrack([(i, j) for i in range(9) for j in range(9) if t[i][j] == 0]):
        print('Done-s')
        return t
    else:
        return False
        print('Done-f')
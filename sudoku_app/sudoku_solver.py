def valid_options(t, i, j):
    if t[i][j] != 0: return set()

    s = set(range(1,10))

    s -= {t[x][j] for x in range(9)}
    s -= {t[i][x] for x in range(9)}

    box_y = i//3
    box_x = j//3
    s -= {t[i][j] for i in range(box_y*3, box_y*3+3)
                  for j in range(box_x*3, box_x*3+3)}
    return s

def solve(t):
    def sestopaj(p):
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
                if sestopaj(p):
                    return True
                t[i][j] = 0 # pomembno
            p.append((i, j))
            return False

    if sestopaj([(i, j) for i in range(9) for j in range(9) if t[i][j] == 0]):
        return t
    else:
        return False
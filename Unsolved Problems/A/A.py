def is_a_beaut(x):
    if len(x) % 3 != 0:
        return False

    combos = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    c = 0

    while c < len(x)-2:
        if x[c:c+2] not in combos:
            return False
        c += 3

s = input()

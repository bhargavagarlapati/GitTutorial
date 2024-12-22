d = dict()
def charcount(s):
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

print(charcount("mississippi"))





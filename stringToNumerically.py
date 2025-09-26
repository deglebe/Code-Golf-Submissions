i,o, n = input(), "", 0
l = i[0]
for I in i:
    if I == l:
        n += 1
    else:
        o += (l + str(n))
        n = 1
    l = I
o += (l + str(n))
print(o)

        
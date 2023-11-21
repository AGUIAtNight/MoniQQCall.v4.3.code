p1 = [1, 2]
p2 = [3, 4]

xielv = abs((p1[1] - p2[1]) / (p1[0] - p2[0] + 1e-5))
if xielv > 0.25 and xielv < 2:
    print(xielv)

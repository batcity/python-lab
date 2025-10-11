numbers = [1, 2, 3, 4, 5, 6, 7]
limit = 20
i = 0

while (n := numbers[i]**2) < limit:
    print(f"{numbers[i]} squared is {n}")
    i += 1
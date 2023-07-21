def listComprehensions(a, b, c, d):
    coordinates = [
        [i, j, k]
        for i in range(a + 1)
        for j in range(b + 1)
        for k in range(c + 1)
        if i + j + k != d
    ]
    return coordinates


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


result = listComprehensions(x, y, z, n)
print(result)

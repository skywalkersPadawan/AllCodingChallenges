def print_rangoli(size):
    # your code goes here
    import string

    alphabet = string.ascii_lowercase

    for i in range(size - 1, 0, -1):
        pattern = "-".join(alphabet[size - 1 : i : -1] + alphabet[i:size])
        print(pattern.center(4 * size - 3, "-"))

    print("-".join(alphabet[size - 1 : 0 : -1]))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)

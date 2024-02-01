def count_substring(string, subString):
    count = 0
    subLen = len(subString)

    for i in range(len(string) - subLen + 1):
        if string[i : i + subLen] == subString:
            count += 1

    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

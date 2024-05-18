import textwrap


def wrap(string, maxWidth):
    return "\n".join(textwrap.wrap(string, maxWidth))


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Enter your code here. Read input from STDIN. Print output to STDOUT
width = 5
c = "H"

# top cone
for i in range(1, width * 2 - 1 + 1, 2):
    print((c * i).center(width * 2 - 1))

# top pillar
for i in range(0, width + 1):
    print((c * width).center(width * 2) + (c * width).center(width * 6))

# middle part
for i in range((width + 1) // 2):
    print((c * width * 5).center(width * 6))

# lower pillar
for i in range(0, width + 1):
    print((c * width).center(width * 2) + (c * width).center(width * 6))

# lower cone
for i in range(width * 2 - 1, -1, -2):
    print((c * i).center((width * 2 - 1 + 1) * 5))


# need to understand how to solve this problem later, need try solving this to understand how to print patterns

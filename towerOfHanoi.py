# Recursive python problem to solve the Tower of Hanoi
def hanoi(n, start, end):
    # Base case
    if (n == 1):
        print(f"{start} -> {end}")

    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        print(f"{start} -> {end}")
        hanoi(n-1, other, end)

hanoi(3, 1, 3)


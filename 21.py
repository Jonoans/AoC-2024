

stones = """
125 17
"""

stones = """
27 10647 103 9 0 5524 4594227 902936
"""

ITERATIONS = 25

stones = [int(x) for x in stones.strip().split(' ')]
next_stones = []
memo = {}

def fill_next(current, stones):
    current_str = str(current)
    current_len = len(current_str)
    if current_len % 2 == 0:
        first = int(current_str[:int(current_len / 2)])
        second = int(current_str[int(current_len / 2):])
        stones.append(first)
        stones.append(second)
    elif current == 0:
        stones.append(1)
    else:
        stones.append(current * 2024)

for _ in range(ITERATIONS):
    for stone in stones:
        fill_next(stone, next_stones)
    stones = next_stones
    next_stones = []
print(len(stones))


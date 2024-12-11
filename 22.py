

stones = """
125 17
"""

stones = """
27 10647 103 9 0 5524 4594227 902936
"""

ITERATIONS = 75

stones = [int(x) for x in stones.strip().split(' ')]
next_stones = []
memo = {}

def get_answer(current, iterations):
    if iterations == 0:
        return 1

    if (current, iterations) in memo:
        return memo[(current, iterations)]

    iterations -= 1
    current_str = str(current)
    current_len = len(current_str)
    if current_len % 2 == 0:
        first = int(current_str[:int(current_len / 2)])
        second = int(current_str[int(current_len / 2):])
        memo[(current, iterations+1)] = get_answer(first, iterations) + get_answer(second, iterations)
    elif current == 0:
        memo[(current, iterations+1)] = get_answer(1, iterations)
    else:
        memo[(current, iterations+1)] = get_answer(current * 2024, iterations)

    return memo[(current, iterations+1)]

answer = 0
for stone in stones:
    answer += get_answer(stone, ITERATIONS)
print(answer)


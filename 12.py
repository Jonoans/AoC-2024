from collections import defaultdict
from typing import DefaultDict, Dict, List, Set, Tuple


puzzle = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

puzzle = """.......................#....#....................#....#..##.##.........................................#...........#...........#..
.............#........................................#....................#............#.......................#............#....
.........#.............#..#....#..........................#.......#.#.......#...............................................##....
..........#....#....................................................#....................#...........#....#.......................
.............#...#....................#...........#.........#...........................#............#............................
..........................................................................................#.....#.......#...................##....
...............................................#.#......#..............#...#...................##...........#....#..#...#.........
..#.................#......#........#......................#.......#...............................#..............................
.........................#...............#.....................................#....#..#..#............................#..........
......................#.................................................................#..........#..............#...#......#....
............................#.....##..........#.....................#..........#..#.......#.......................................
......#...###...........#.................................................................#.......................................
......................#.#..#................#..........#................#...........#............#..............#...#.........#...
....#.........................#..#...............................................#....#.............#.............................
..#............#...#............#..........#...............#.....#....##.........................#........#.......................
..................#............#..............#..........................................................#..#..#........#.........
.......#...#............#..........................................................#..............................#.............#.
..#................#....................#.#...#.................................#.........#....................#.........#........
...................................#..#..........................#........#.....#.........................................#.......
...........##.................##............#................#...#..................................##...#........................
..............#..................#....................................................................#...........................
.#...#....#..........##..................................#.............................................................#......#...
......#.....#................................#...............................................................#......#.............
..........#.............................................#............................##....#.........................#............
..........#......#.................#...#........#...........#.#..........#........#....................................#..........
.#..................#.#............................#.......................#.........#.......#....................................
.....................#....#..................#..................................................##..#................#............
......#......................#..#..............##.......#..................................................#..............#.......
..........................................................................#........#...#..............#.................#.........
....................##....#.......................#........#...................#.............##.......#...........................
.........#............#..................................................................................#........................
........................................................................#................#........................#.............#.
............#.......#.................................#............#..............................................................
.#.............#...............................................#....#.........#....#..................................#.#.........
.......................................#.....................................................................................#....
........#........................................#...............#........................................................#.......
...............................#.........#........#...........#.......................................................#.........#.
.....................##...#....................................................#............#..................#..#..........##...
................#..........#...#............................................................#...##................................
...................#........#...............................#.................#.........#.........................................
.................................................................................................................#................
............................#......................................................#.....................................#......#.
......#................#............................#.............................................................................
..#...........#.....#.........#....#................#............................................#................................
..................................#.......#.......#...........#.........#................#.....................................#.#
...............................................#............................................#.#.....................#.......##....
..............................#...............#..............................#...#...#.............................#...........#..
.......#...........#..........................................................#........#..#.........#.....#.....#...#.............
......................................................#.#............#.........#.#...........#........##.....#....................
...........................................................................#..........#.........................#.........#.......
....#.........................#.....................................................................................#...#......#..
...#.......#............................................................#...............................#....................##.#.
.................................#.....#................................................................#.........................
.....................................#........................#....................................#..............................
..............#.......................................................................#.......#....................#..........#...
................................#..........................................#.................................#.....#..............
...........#.......................................................#...............#.....................#..............#......#..
..................................#..........................#.................................................................#..
.............##......#....................................................#......#...............................................#
#.......#...................#..........#...................#.................#..................................................#.
.......#..........#.....##...........#.......................#............#..............................#.............#..........
.............#...................##......................................................................................#........
#.............................#...................................................................#...............................
.#...................................#....##..................................................................................#...
.................................#.#..................#..#..#..........................#.......#..................................
..................#....#....#....................................................#....................................#........#..
..........................................#...#.....#...........#.........#............#............#..........................#..
...............................................................................#..............................................#...
.............................#......#....................#....#....................................................#.#.#..........
................##......#........#........#...........#..........................#......................#..............#..........
.....................#.....#..#.............................................................................................#.....
.......#..#...........#................................................................#..........................................
#.......................................................................................................#...#.....................
.#..........................................................#.....................................................#...............
#.....#...#...............#..#......#........#..#...................#...................#.................#.......................
..#.................................................................................#.#......................#....................
.......................#.............#..........#.......................#...................................#.....................
.................#......#......#...#.#.#.............................#.......................................................#....
..#...........................................................................................................#...................
.................................#..................#.....#........#.........................................................#....
.............#......................#...............................................#...#.............................#...#....#..
.#............................#..........................#.#...........................#..........................#.#.............
.............................#.........#.................##............................#...................#......................
.........#......#....#.........#..............................................................................................#..#
.....................#......#.................#..#..........................#..................#..............................#.#.
........................................................#......................#............#.......#......#......................
........................................#....##.#........#......#..............................#..........#..........#.##.........
.............#.......#.......#......................#..........................................#.........#............#...#...#.#.
..................#........................................................#...............................#.....#.....#..........
.........#.................#........#..............^..............#.................##......#...................................#.
....#...................#.#.................................#...#.................................................#...............
.................#.............................................#................#.....#......#.......#...................#........
...............#...............................................................................#..#...............#...............
........................................##..........................................................................##............
............................................#...................#........#...#...#....#.........#...................#.............
.....#...#...................#....................................#......#...........#...............#............................
........................#..................#.....................#.................................................#......##......
...#.................#....................#..................................#.#.........................#.......#................
....................#............#..................................#...#......#....................#...............#.............
.....#...............#.......###........#............#......................#.......#....#........................................
....................#........#...........#..................................#..#................#.............#...................
.....#..................#...................#.#..................................#.......#..#.....................................
..#..#.......#........................................#.................................................................#.........
.......#............#...#....#.......................#.#...................................#.........................#..#.#.......
..............#......................................................................................................#............
............#....................#........................#.........#...#.........................................................
...................................#..............................#.........................................................#.....
......##...........#.#........................#.........................................................................#.........
..........................#.....................................................#..............................#..............#...
.........................#...#.....................#..#................#................................................#....#....
...#.................................#...#.......#...............................................................#................
..................................#....................................#...........................##..#.#.....................#..
.#.............#.....#...............................................................#...............#...............#..#.........
.........#.............................#........................#.............#......................#........#............#......
...................................#..#...#.....................................#.................................................
........................................##..........#..............................................#.....................#........
......#...........................................#....#.....................#...................#..#.........#...................
.#....#.....#........##..................................#......#................................................#....#..##.......
..........#....................................................................##.........................#...........#...........
...........#.#......#.......#..................#............#...............................................#...#..............#..
.................................................................#.......#.........#.....#........#....##....#..........#.........
.............................#......................................................#.....#...#...#....#...........#..........#.#.
.....................#........#.........................#......................................#................#...............#.
.........................................................................#...................................................#....
..............#...#..#................#....................................#.......#....#.#...............#.........#.............
.......#......#.#............................................#.......#............................................................
##......................................................#..#.................................##...................#..#...........#
...........#.#...#........#............#..............................#........................#.........................#..#.....
................................................##.........................................#.................#....................
............................#....................................................#...#........................#.#......#........#."""

original_puzzle = puzzle
puzzle = puzzle.splitlines()
x_max = len(puzzle)
y_max = len(puzzle[0])
x_oob = lambda coord: coord[0] < 0 or coord[0] >= x_max
y_oob = lambda coord: coord[1] < 0 or coord[1] >= y_max

guard_position = (-1, -1)
obstacle_x = defaultdict(set)
obstacle_y = defaultdict(set)
for x in range(x_max):
    for y in range(y_max):
        if puzzle[x][y] == '^':
            guard_position = (x, y)
            break
        elif puzzle[x][y] == '#':
            obstacle_x[x].add(y)
            obstacle_y[y].add(x)

    if guard_position != (-1, -1):
        break

dir = (-1, 0)
def turn_right(curr_dir: Tuple[int, int]):
    return (curr_dir[1], -curr_dir[0])

visited = set()
original_guard = guard_position
while True:
    while not (x_oob(guard_position) or y_oob(guard_position)) and puzzle[guard_position[0]][guard_position[1]] != '#':
        guard_position = tuple(map(lambda v: v[1] + dir[v[0]], enumerate(guard_position)))
        visited.add(guard_position)

    visited.remove(guard_position)
    if x_oob(guard_position) or y_oob(guard_position):
        break

    guard_position = tuple(map(lambda v: v[1] - dir[v[0]], enumerate(guard_position)))
    dir = turn_right(dir)

count = 0
puzzle = [[x for x in s] for s in original_puzzle.splitlines()]
while visited:
    current_visited = set()
    guard_position = original_guard
    dir = (-1, 0)

    x, y = visited.pop()

    puzzle[x][y] = '#'
    looped = False
    while not looped:
        while not (x_oob(guard_position) or y_oob(guard_position)) and puzzle[guard_position[0]][guard_position[1]] != '#':
            guard_position = tuple(map(lambda v: v[1] + dir[v[0]], enumerate(guard_position)))
            if (*guard_position, *dir) in current_visited:
                looped = True
                break
            current_visited.add((*guard_position, *dir))

        if looped:
            break

        current_visited.remove((*guard_position, *dir))
        if x_oob(guard_position) or y_oob(guard_position):
            break

        guard_position = tuple(map(lambda v: v[1] - dir[v[0]], enumerate(guard_position)))
        dir = turn_right(dir)

    if looped:
        count += 1
    puzzle[x][y] = '.'
print(count)
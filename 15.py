from collections import defaultdict

puzzle = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

puzzle = """
................................y.................
............9.....Q................y..............
..................................................
..................................................
..........Q.......................x..N..1.........
.....9......6.e......................x.......j....
............e..x6Q9...............................
...........6..................................j...
...e....................................j.........
.............Q8.......................x..1........
.....w.......8...................y................
..n.......................y...................s...
.n................................................
.........n...............e........................
8..C..............r.....F......................j..
.......C......................................1..s
................n.u..................W...t........
......w..........r.........W..5J..................
.....p..............................J.............
.....T.................................d..........
......prw................uW.....Z.....t..6........
....p.r.....f............7........................
........C.f...q..................3.Y..............
.......w.f..........M.....C..5.......t............
....S..f.q.........................5..............
.............p......J........c................Z...
......................5...........................
....T...........u........D.....8........R.........
..0....T.............7M..........J....RZ..........
......t.Iu......................P.......W..Z......
...............D.......M.....i.......z..........s.
...........F..DM..q............R..................
........T....0............................c....s..
.E........0..............N........................
.......................................1........2X
..........Y....0.q....F..................X........
...............F.I..........................X.....
....U......z..............7i.........S..c.........
E.D..S...............................4.....2......
..S.........z..I......i.........m.............2...
.......E............I.....i..................R....
..................N...............................
....................................m.............
...Y...............P.............m...2............
................N...z................c............
.......................................4..........
........U.........P...............7..d..........4.
........................X....3....d...............
Y................P.U..........3...........d.......
...U..................................3...........
"""

puzzle = puzzle.strip().splitlines()

x_max = len(puzzle[0])
y_max = len(puzzle)
y_antennas = defaultdict(lambda: defaultdict(set))

for y in range(y_max):
    for x in range(x_max):
        if puzzle[y][x] != '.':
            y_antennas[puzzle[y][x]][y].add(x)

positions = set()
for y in range(y_max):
    for x in range(x_max):
        distance = int((max(y_max-y-1, y-0) + 1) / 2)
        for diff in range(0, distance):
            y_low = y - diff
            y_low_t = y_low - diff
            y_high = y + diff
            y_high_t = y_high + diff

            for ant_type, antennas in y_antennas.items():
                if y_low_t >= 0:
                    curr_row_antennas = antennas[y_low]
                    twice_row_antennas = antennas[y_low_t]
                    for ant_x in curr_row_antennas:
                        twice_x = (x + (ant_x - x) * 2)
                        if ant_x != twice_x and twice_x in twice_row_antennas:
                            positions.add((y, x))

                if y_high_t < y_max:
                    curr_row_antennas = antennas[y_high]
                    twice_row_antennas = antennas[y_high_t]
                    for ant_x in curr_row_antennas:
                        twice_x = (x + (ant_x - x) * 2)
                        if ant_x != twice_x and twice_x in twice_row_antennas:
                            positions.add((y, x))


print(len(positions))
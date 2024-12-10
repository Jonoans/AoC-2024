trail_map = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

trail_map = """
3265810567887610176543232112345687657894520112310124343
2178923456998543289432103001236799548765011201459835432
3069434541047654343234304320189878039454324301267746301
4454108932432105010145215617654360124565015892398657412
5643237658347892189256789708763254103876546765489018543
6762100549856783478765499899100123212981237894376529234
9854001236765898543287306789230345101870892143489430143
0123112345654387620196215276541236989896781002438321056
1434876014567821212305454108910107858785432211320123987
0567945623001930101414303267671098965676128340210784326
1498732782122341210523412156782367874301039654325695012
2389601095673234387674323045093450123212078769784596876
1234515214984105498987634532112345219890198578693287945
0145656303345096567898549601004876308763287657580176532
1098745432296787450103438712345965438654346578432985401
7887676501187698321212397103896876129860145569371092310
6998389010067897454323788234887623078101233401287601223
5467210327150156565610639948901012365265432314396540834
0354343478943241078776548857612103454374301015893239985
1298123567784332189789037766523328968989210126782178876
4567034987694323476570126345435410871874323010561065710
3089215676543210565234105430456701980165012123479874321
2176304321031012910165234521367812341298783012980675012
0125455890123329879874678901298989850345694503321589654
1234126787001456765983107103456548766546587678932456783
5434034576102345651012236012767632667632109765449321092
6543467601234450141201345989898601898123678896358015601
7612398532985983230345787671087789621014561201267454789
8500120123876876567896094562545656789865010212102363210
9145034534560745456987123043876549898774321347821078101
1036765325671234547891212156965030105689833456901239821
0129896010787565432180301207834121234387658921010143210
2345687321895679001015401210121010567896567432987656978
1066787438986988120876232349854101454987436543478967869
9876096567630177638980143458063243043890122132567876554
0945143452123210543987652967178952132101021091478745043
1234232143010349898801201873297867873018962780369432132
1233245056725656789754343234983458962103873676214345671
0340196549834765608763452105672018743012964501108210980
0658287654234897512014569010121029654523455612989432126
1789808903145698763123678101291234549623896543076501087
2565419012098765454094983214380165438712387054123457898
3476320121010894345785670305678078329603432189014766527
4989689032101923296654321494109989012506545673456895412
7676788543432010187105656583212098103417656012187659303
8545097656589101045234783672103107894328321043098748212
9432165409677816676543294543014236765019410452129237326
0121670318761965589430123678985345891054569567932106587
7650181229650874594321210789076256702143678398867603496
8542397834541123671010012698123105213432121210768712345
9231456998432010789898763283434554396541030123459632434
2110765107322989690176654196543676787612345014568541023
2019894236011878521085545087212987988901456905873456911
1238763245010965430294236789803101876216767876912367800
0145632100123454340123107898714312345665898965101054321
"""

trail_map = [[int(y) for y in x] for x in trail_map.strip().splitlines()]
y_max = len(trail_map)
x_max = len(trail_map[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

explore = []
for y in range(y_max):
    for x in range(x_max):
        if trail_map[y][x] == 0:
            s = set()
            s.add((y, x))
            explore.append((y, x, s))


score = 0
while explore:
    y, x, visited = explore.pop()
    val = trail_map[y][x]
    if val == 9:
        score += 1
        continue

    val += 1
    for (new_y, new_x) in directions:
        new_y += y
        new_x += x
        if new_y < 0 or new_y >= y_max or new_x < 0 or new_x >= x_max or trail_map[new_y][new_x] != val:
            continue

        if (new_y, new_x) not in visited:
            explore.append((new_y, new_x, visited))
            visited.add((new_y, new_x))
print(score)

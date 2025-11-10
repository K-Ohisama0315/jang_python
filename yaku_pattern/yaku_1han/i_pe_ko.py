import const

def check_i_pe_ko(formed_hand, menzen) -> bool:
    """
    手牌が一盃口か判定する
    """
    # 門前でなければFalseを返す
    if menzen == False:
        return False

    a = []

    hand = formed_hand["hand"]

    # 鳴いている場合（手牌が4枚未満の時）、Falseを返す
    if len(hand) != 4:
        return False

    # 手牌が三枚で構成されているか判定する
    for pairs in hand:
        if len(pairs) == 3:
            a.append(pairs)
    
    # 数値に変換した手牌を格納するリスト
    mentsu_hand = []

    # 手牌を数値に変換する
    for mentsu in a:
        num_mentsu = []

        for tile in mentsu:
            num = const.tiles[tile]

            if num < 30:  # 字牌でない場合のみ変換  
                num_mentsu.append(num)

            else:   # 字牌の場合はスキップ
                continue

        if len(num_mentsu) != 0:
            mentsu_hand.append(num_mentsu)
    
    # 順子を格納するリスト
    shuntsu_hand = []

    # 順子であるか判定する
    for b in mentsu_hand:
        if (b[0] + 1 == b[1] and b[1] + 1 == b[2]):
            shuntsu_hand.append(b)
            
    # 一盃口であるか判定する
    for c in shuntsu_hand:
        # 順序が完全に一致する重複を探す
        i_pe_ko_hand = set(tuple(x) for x in shuntsu_hand)
    
    # 一盃口であれば、順子の数と重複を除いた順子の数が異なる
    if len(i_pe_ko_hand) != len(shuntsu_hand):
        return True
    else:
        return False

formed_hand = {"hand":[["1m","2m","3m"],["1m","2m","3m"],["5s","6s","7s"],["east","east","east"]],"head":["8m","8m"]}
menzen = True
print(check_i_pe_ko(formed_hand, menzen))
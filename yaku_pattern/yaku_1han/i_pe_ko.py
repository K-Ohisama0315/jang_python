import const

def check_i_pe_ko(formed_hand, menzen) -> bool:
    """
    手牌が一盃口か判定する
    """
    # 門前でなければFalseを返す
    if menzen == False:
        return False

    hand = formed_hand["hand"]
    
    # 数値に変換した手牌を格納するリスト
    mentsu_num_hand = []

    # 手牌を数値に変換する
    for mentsu in hand:
        mentsu_num = []

        for tile in mentsu:
            num = const.tiles[tile]

            if num < 30:  # 字牌でない場合のみ変換  
                mentsu_num.append(num)

            else:   # 字牌の場合はスキップ
                continue

        mentsu_num_hand.append(mentsu_num)
    
    # 順子を格納するリスト
    shuntsu_hand = []

    # 順子であるか判定する
    for tile in mentsu_num_hand:
        if (tile[0] + 1 == tile[1] and tile[1] + 1 == tile[2]):
            shuntsu_hand.append(tile)
            
    # 一盃口であるか判定する
    for tile in shuntsu_hand:
        # 順序が完全に一致する重複を探す
        i_pe_ko_hand = set(tuple(tile) for tile in shuntsu_hand)
    
    # 一盃口であれば、順子の数と重複を除いた順子の数が異なる
    if len(i_pe_ko_hand) != len(shuntsu_hand):
        return True
    else:
        return False

formed_hand = {"hand":[["1m","2m","3m"],["1m","2m","3m"],["5s","6s","7s"],["east","east","east"]],"head":["8m","8m"]}
menzen = True
print(check_i_pe_ko(formed_hand, menzen))
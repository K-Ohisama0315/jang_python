sangen_tile = ["white", "green", "red"]

def check_daisangen(formed_hand, call_tile) -> str:
    """
    大三元が成立するか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in call_tile:
        hand.append(mentsu)

    # 刻子を抽出する
    kotsu = []
    for mentsu in hand:
        if mentsu[0] == mentsu[1] == mentsu[2]:
            kotsu.append(mentsu)
    
    # 刻子の中に三元牌があれば集合に追加
    sangen_set = set()
    for tile in kotsu:
        if tile[0] in sangen_tile:
            sangen_set.add(tile[0])
    
    # 三元牌の集合の要素数が3であれば大三元成立
    if len(sangen_set) == 3:
        return "daisangen"
    
    # 三元牌の集合の要素数が2の時
    if len(sangen_set) == 2:
        head = formed_hand["head"]
        # アタマが三元牌であれば小三元成立 
        if head[0] in sangen_tile and head[0] not in sangen_set:
            return "shousangen"
    
    # それ以外は不成立
    return None
    
hand_set = {"hand":[["red","red","red"],["4m","5m","6m"],["7m","8m","9m"],["1s","2s","3s"]],"head":["5s","5s"]}
call_tile = [["white","white","white"],]
print(check_daisangen(hand_set, call_tile))
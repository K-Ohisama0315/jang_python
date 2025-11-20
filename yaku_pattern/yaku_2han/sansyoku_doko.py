def check_sansyoku_doko(formed_hand, formed_call) -> bool:
    """
    三色同刻が成立するか判定する
    """
    hand = formed_hand["hand"].copy()

    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)

    # 刻子を判定し、色と数字に分けた後タプルに代入して、それをリストに格納する
    kotsu_list = []
    for mentsu in hand:
        if mentsu[0] == mentsu[1] == mentsu[2]:
            color = mentsu[0][0:1]
            value = mentsu[0][1:2]
            kotsu_list.append((color, value))
    
    # 数字ごとに色を集合に格納し、それを辞書で表現する
    kotsu_set = {}
    for list in kotsu_list:
        kotsu_set.setdefault(list[0], set()).add(list[1])
    
    # 数字ごとに3色揃っているか判定する
    for kotsu in kotsu_set:
        if len(kotsu_set[kotsu]) >= 3:
            return True
    
    return False

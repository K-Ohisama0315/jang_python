def check_sansyoku_doko(formed_hand, call) -> bool:
    """
    三色同刻が成立するか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for tile in call:
        hand.append(tile)

    # 刻子を判定し、色と数字に分けた後タプルに代入して、それをリストに格納する
    kotsu_list = []
    for pair in hand:
        if pair[0] == pair[1] == pair[2]:
            color = pair[0][0:1]
            value = pair[0][1:2]
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

hand_set = {"hand":[["2m","2m","2m"],["1s","1s","1s"],["1p","1p","1p"]],"head":["8m","8m"]}
call = [["1m","1m","1m"],]
print(check_sansyoku_doko(hand_set, call))
def check_zihuhai(formed_hand, call, jikaze) -> bool:
    """
    自風牌が3つ以上あり、役が成立するか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in call:
        hand.append(mentsu)

    # 自風牌が3枚以上あればTrueを返す
    for mentsu in hand:
        count = 0
        for tile in mentsu:
            if tile == jikaze:
                count += 1
        if count >= 3:
            return True
    return False

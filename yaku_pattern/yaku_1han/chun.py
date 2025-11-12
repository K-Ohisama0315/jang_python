def check_chun(formed_hand, call) -> bool:
    """
    手牌に中が３枚あるか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in call:
        hand.append(mentsu)

    # 中が3枚以上あればTrueを返す
    for mentsu in hand:
        count = 0
        for tile in mentsu:
            if tile == "red":
                count += 1
        if count >= 3:
            return True
    return False
def check_chun(formed_hand, call) -> bool:
    """
    手牌に中が３枚あるか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for tile in call:
        hand.append(tile)

    # 中が3枚以上あればTrueを返す
    for pair in hand:
        count = 0
        for tile in pair:
            if tile == "red":
                count += 1
        if count >= 3:
            return True
    return False
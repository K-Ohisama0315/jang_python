def check_zihuhai(hand_set, jikaze) -> bool:
    """
    自風牌が3つ以上あり、役が成立するか判定する
    """
    hand = hand_set["hand"]

    # 自風牌が3枚以上あればTrueを返す
    for pair in hand:
        count = 0
        for tile in pair:
            if tile == jikaze:
                count += 1
        if count >= 3:
            return True
    return False

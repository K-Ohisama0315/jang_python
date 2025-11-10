def check_bahuhai(hand_set, bakaze) -> bool:
    """
    手牌に場風牌が３枚以上あり、役が成立するか判定する
    """
    hand = hand_set["hand"]

    # 場風牌が3枚以上あればTrueを返す
    for pair in hand:
        count = 0
        for tile in pair:
            if tile == bakaze:
                count += 1
        if count >= 3:
            return True
    return False
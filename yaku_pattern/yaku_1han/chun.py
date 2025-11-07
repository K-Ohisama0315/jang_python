def check_chun(hand_set) -> bool:
    """
    手牌に中が３枚あるか判定する
    """
    hand = hand_set["hand"]

    # 中が3枚以上あればTrueを返す
    for pair in hand:
        count = 0
        for tile in pair:
            if tile == "red":
                count += 1
        if count >= 3:
            return True
    return False
def check_hatsu(hand_set) -> bool:
    """
    手牌に発が３枚あるか判定する
    """
    hand = hand_set["hand"]

    # 発が3枚以上あればTrueを返す
    for pair in hand:
        count = 0
        for tile in pair:
            if tile == "green":
                count += 1
        if count >= 3:
            return True
    return False
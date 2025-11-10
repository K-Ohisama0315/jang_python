def check_haku(formed_hand, call) -> bool:
    """
    手牌に白が３枚あるか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for tile in call:
        hand.append(tile)

    # 白が3枚以上あればTrueを返す
    for pair in hand:
        count = 0
        for tile in pair:
            if tile == "white":
                count += 1
        if count >= 3:
            return True
    return False

formed_hand = {"hand":[["white","white","white"],["1m","2m","3m"],["5s","6s","7s"],["6s","7s","8s"]],"head":["8m","8m"]}
call = []
print(check_haku(formed_hand, call))
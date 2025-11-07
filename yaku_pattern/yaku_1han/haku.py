def check_haku(hand_set) -> bool:
    """
    手牌に白が３枚あるか判定する
    """
    hand = hand_set["hand"]

    # 白が3枚以上あればTrueを返す
    for pair in hand:
        count = 0
        for tile in pair:
            if tile == "white":
                count += 1
        if count >= 3:
            return True
    return False

hand_set = {"hand":[["white","white","white"],["1m","2m","3m"],["5s","6s","7s"],["6s","7s","8s"]],"head":["8m","8m"]}
print(check_haku(hand_set))
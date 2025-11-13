def check_bahuhai(formed_hand, call, bakaze) -> bool:
    """
    手牌に場風牌が３枚以上あり、役が成立するか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in call:
        hand.append(mentsu)

    # 場風牌が3枚以上あればTrueを返す
    for mentsu in hand:
        count = 0
        for tile in mentsu:
            if tile == bakaze:
                count += 1
        if count >= 3:
            return True
    return False

formed_hand = {"hand":[["1m","2m","3m"],["5s","6s","7s"],["6s","7s","8s"]],"head":["8m","8m"]}
call = [["east","east","east"],]
print(check_bahuhai(formed_hand, call, "east"))
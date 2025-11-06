YAOCHUHAI_INDICES = ("1p", "9p", "1s", "9s", "1m", "9m",
                    "east", "south", "west", "north", 
                    "white", "green", "red")

def check_tanyao(hands_set) -> bool:
    """
    手牌がタンヤオか判定する
    """
    hand = hands_set["hand"]
    head = hands_set["head"]

    # アタマとそれ以外の手牌を一つのリストにまとめる
    hand.append(head)

    # リスト内に么九牌がないか確認する
    for pair in hand:
        for p in pair:
            for q in YAOCHUHAI_INDICES:
                if p == q:
                    return False
    return True

hand_set = {"hand":[["1m","2m","3m"],["1m","2m","3m"],["5s","6s","7s"],["6s","7s","8s"]],"head":["8m","8m"]}

print(check_tanyao(hand_set))
kokushimusou_pattern = ("1p", "9p", "1s", "9s", "1m", "9m",
                    "east", "south", "west", "north", 
                    "white", "green", "red")

def check_kokushimusou(hands_set) -> bool:
    """
    手牌が国士無双かどうか判定する

    :param:hand_set 手牌パターン
    :return: bool
    """
    hands_pattern = hands_set["hand"]

    # 国士無双のパターンに当てはまる牌を格納する空集合
    kokushimusou_set = set()
    
    # 手牌と国士無双の牌を照らし合わせるループ処理
    for hand_tile in hands_pattern:
        for kokushi_tile in kokushimusou_pattern:

            # 手牌が国士無双のパターンに合う牌であれば、集合に代入する
            if hand_tile == kokushi_tile:
                kokushimusou_set.add(hand_tile)
    
    print(kokushimusou_set)

hands_set = {"first":["1p", "2p", "9s", "8m", "east", "east"], "second":{"4p", "1s"}}
check_kokushimusou(hands_set)




YAOCHUHAI_INDICES = ("1p", "9p", "1s", "9s", "1m", "9m",
                    "east", "south", "west", "north", 
                    "white", "green", "red")

def check_tanyao(formed_hand, formed_call) -> bool:
    """
    手牌がタンヤオか判定する
    """
    hand = formed_hand["hand"]
    head = formed_hand["head"]

    # アタマとそれ以外の手牌を一つのリストにまとめる
    hand.append(head)
    
    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)

    # リスト内に么九牌がないか確認する
    for mentsu in hand:
        for tile in mentsu:
            for tile_yaochuhai in YAOCHUHAI_INDICES:
                if tile == tile_yaochuhai:
                    return False
    return True
import const

def check_ryan_peekou(menzen, formed_hand) -> str:

    # 面前でなければNoneを返す
    if not menzen:
        return None
    
    hand = formed_hand["hand"].copy()

    # 手牌の情報を数値に変換する
    numbered_hand = const.change_hand_to_num(hand)

    # 順子であるか判定し、順子であればリストに格納する
    shuntsu_list = []
    for mentsu in numbered_hand:
        if const.find_shuntsu(mentsu):
            shuntsu_list.append(mentsu)
    
    # 一盃口、二盃口が成立するか判定する
    finish_hand = []
    for tile in shuntsu_list:
        # 順序が完全に一致する重複を探す
        finish_hand = set(tuple(tile) for tile in shuntsu_list)
    
    # 一盃口、二盃口であれば、順子の数と重複を除いた順子の数が異なる
    # 二盃口の判定
    if len(shuntsu_list) - len(finish_hand) == 2:
        return "二盃口"
    # 一盃口の判定
    elif len(shuntsu_list) - len(finish_hand) == 1:
        return "一盃口"
    else:
        return None




import collections

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
    
    # 面子をタプルに置き換える
    shuntsu_tuple = [tuple(mentsu) for mentsu in shuntsu_list]

    # 面子の種類ごとにカウントする
    shuntsu_counter = collections.Counter(shuntsu_tuple)

    # 2で割った時の値(整数部分)を見ることでペア数をカウントする
    pair_count = sum(mentsu_count // 2 for mentsu_count in shuntsu_counter.values())

    if pair_count == 2:
        return "二盃口"
    elif pair_count == 1:
        return "一盃口"
    else:
        None




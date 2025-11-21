yaku_hai = {"役牌：白":"white", "役牌：發":"green", "役牌：中":"red", "役牌：自風牌":"", "役牌：場風牌":""}

# 役牌判定関数
def check_yaku_hai(jikaze, bakaze, formed_hand, formed_call) -> dict:

    # 役牌の辞書に自風、場風を追加する
    yaku_hai["役牌：自風牌"] = jikaze
    yaku_hai["役牌：場風牌"] = bakaze

    hand = formed_hand["hand"].copy()

    yakuhai_set = set()
    
    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)

    # 面子の先頭を追加(役牌は刻子、槓子にしかならないため)
    target = {mentsu[0] for mentsu in hand}

    # マッチするものを集合に格納
    yakuhai_set = {k for k, v in yaku_hai.items() if v in target}

    # # 役ごとに刻子ができているか判定する
    # for mentsu in hand:
    #     for key, yaku in yaku_hai.items():
    #         count = 0
    #         for tile in mentsu:
    #             if tile == yaku:
    #                 count += 1
                
    #         if count >= 3:
    #             yaku_dict[key] = True
    
    return yakuhai_set
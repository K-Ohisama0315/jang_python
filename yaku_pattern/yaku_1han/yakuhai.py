yaku_hai = {"white":"white", "green":"green", "red":"red", "jikaze":"", "bakaze":""}

# 役牌判定関数
def check_yaku_hai(jikaze, bakaze, formed_hand, formed_call) -> dict:

    # 役牌の辞書に自風、場風を追加する
    yaku_hai["jikaze"] = jikaze
    yaku_hai["bakaze"] = bakaze

    hand = formed_hand["hand"].copy()

    yaku_dict = {"white":False, "green":False, "red":False, "jikaze":False, "bakaze":False}
    
    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)

    # 役ごとに刻子ができているか判定する
    for mentsu in hand:
        for key, yaku in yaku_hai.items():
            count = 0
            for tile in mentsu:
                if tile == yaku:
                    count += 1
                
            if count >= 3:
                yaku_dict[key] = True
    
    return yaku_dict
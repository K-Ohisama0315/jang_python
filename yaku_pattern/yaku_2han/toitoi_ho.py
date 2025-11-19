def check_toitoi_ho(formed_hand, formed_call) -> bool:

    hand = formed_hand["hand"]

    # 副露牌を手牌に追加する
    for mentsu in formed_call:
        hand.append(mentsu)

    # 手牌がすべて刻子でできているか判定する
    toitoi_flg = True
    for mentsu in hand:
        for tile in mentsu:
            if mentsu[0] != tile:
                toitoi_flg = False
    
    if toitoi_flg == True:
        return True

    return False
    
    
def check_ikkitsuukann(formed_hand, formed_call) -> bool:
    """
    一気通貫が成立するか判定する関数
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)

    # 順子のみを抽出する
    shuntsu = []
    for mentsu in hand:
        if mentsu[0] != mentsu[1]:  # 順子の場合
            shuntsu.append(mentsu)
    
    # 牌の種類を抽出する
    types = set()
    for mentsu in shuntsu:
        tile_type = mentsu[0][-1]  # 牌の種類を取得
        if "m" in tile_type:
            types.add("m")
        elif "p" in tile_type:
            types.add("p")
        elif "s" in tile_type:
            types.add("s")
    
    # 一気通貫が成立するか判定
    for type in types:
        has_1 = False   
        has_4 = False
        has_7 = False
        for mentsu in shuntsu:
            if mentsu[0] == "1" + type: # 面子が（1, 2, 3）の場合
                has_1 = True
            elif mentsu[0] == "4" + type:   # 面子が（4, 5, 6）の場合
                has_4 = True
            elif mentsu[0] == "7" + type:   # 面子が（7, 8, 9）の場合
                has_7 = True

        if has_1 and has_4 and has_7:   # 一気通貫が成立
            return True

    return False
            
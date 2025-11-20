yaochuu_tiles = ["1m", "9m", "1p", "9p", "1s", "9s",
                 "east", "south", "west", "north",
                 "white", "green", "red"]

zihai_tiles = ["east", "south", "west", "north",
                 "white", "green", "red"]

def check_jun_chanta(formed_hand, formed_call) -> str:
    """
    純全帯么九、混全帯么九が成立するか判定する関数
    """
    hand = formed_hand["hand"].copy()

    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)
    
    # 面子に么九牌が含まれているか確認
    chanta = []
    for mentsu in hand:
        for tile in mentsu:
            chanta_flag = False

            if tile in yaochuu_tiles:
                chanta_flag = True  # 么九牌が含まれている場合、フラグをTrueにする
                break

        if chanta_flag:     # 么九牌が含まれている場合、その面子をリストに追加
            chanta.append(mentsu)
    
    # 雀頭に么九牌が含まれている場合
    if formed_hand["head"][0] in yaochuu_tiles:
        chanta.append(formed_hand["head"])
    
    # 么九牌が含まれる面子が5種類未満の場合は、純全帯么九・混全帯么九は成立しない
    if len(chanta) < 5:
        return None
    
    # 純全帯么九か混全帯么九かを判定
    # 面子の判定
    jun_chanta = []
    for mentsu in hand:
        if mentsu[0] not in zihai_tiles:
            jun_chanta.append(mentsu)
    
    # 雀頭の判定
    if formed_hand["head"][0] not in zihai_tiles:
        jun_chanta.append(formed_hand["head"])
    
    if len(jun_chanta) == 5:
        return "純全帯么九"
    else:
        return "混全帯么九"
    

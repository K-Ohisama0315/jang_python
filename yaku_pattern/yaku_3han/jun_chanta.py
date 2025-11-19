yaochuu_tiles = ["1m", "9m", "1p", "9p", "1s", "9s",
                 "east", "south", "west", "north",
                 "white", "green", "red"]

def check_jun_chanta(formed_hand, formed_call) -> str:
    """
    純全帯么九、混全帯么九が成立するか判定する関数
    """
    hand = formed_hand["hand"]

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
    for tile in yaochuu_tiles:
        if formed_hand["head"][0] == tile:
            chanta.append(formed_hand["head"])
    
    # 么九牌が含まれる面子が5種類未満の場合は、純全帯么九・混全帯么九は成立しない
    if len(chanta) < 5:
        return None
    
    # 純全帯么九か混全帯么九かを判定
    kotsu_count = 0
    for mentsu in chanta:
        if mentsu[0] == mentsu[1]: # 刻子の場合(雀頭も判定に含むため、1番目と2番目のみを比較)
            kotsu_count += 1
    
    if kotsu_count == 5:
        return "純全帯么九"
    else:
        return "混全帯么九"
    

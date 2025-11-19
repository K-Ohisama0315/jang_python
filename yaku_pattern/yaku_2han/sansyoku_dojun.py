import const

def check_sansyoku_dojun(formed_hand, formed_call) -> bool:
    """
    三色同順の判定を行う関数
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)
    
    # 手牌の情報を数値に変換する
    numbered_hand = const.change_hand_to_num(hand)
    
    # 順子を判定する
    shuntsu_num_list = []
    for mentsu in numbered_hand:
        if const.find_shuntsu(mentsu):
            shuntsu_num_list.append(mentsu)
    
    # 順子の最初の数字を抽出する
    shuntsu_start_num_set = set()
    for shuntsu in shuntsu_num_list:
        shuntsu_start_num_set.add(shuntsu[0] % 10)
    
    # 順子ごとに牌の色を集合に格納する
    sansyoku = {}
    for shuntsu_start_num in shuntsu_start_num_set:
        tile_type_set = set()
        for shuntsu in shuntsu_num_list:
            if shuntsu[0] % 10 == shuntsu_start_num:
                tile_type_set.add(shuntsu[0] // 10)
        
        sansyoku[shuntsu_start_num] = tile_type_set
    
    # リスト内の集合の要素が3個あるとき、三色同順が成立していると判定する
    for mentsu in sansyoku:
        if len(sansyoku[mentsu]) == 3:
            return True
    
    return False

                



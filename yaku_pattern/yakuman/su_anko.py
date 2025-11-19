# 三暗刻、四暗刻、四暗刻単騎を判定する関数
def check_su_anko(formed_hand) -> str:

    hand = formed_hand["hand"]
    wait = formed_hand["wait"]

    # 暗刻がいくつあるかカウントする
    anko_count = 0
    for mentsu in hand:
        tile_count = 0
        for tile in mentsu:
            if mentsu[0] == tile:
                tile_count += 1
        
        if tile_count >= 3:
            anko_count += 1
    
    # 四暗刻単騎の場合
    if anko_count == 4 and wait == "tanki":
        return "四暗刻単騎"
    
    # 四暗刻の場合
    if anko_count == 4:
        return "四暗刻"
    
    # 三暗刻の場合
    if anko_count == 3:
        return "三暗刻"
    
    # 暗刻が3つ未満の場合
    return None
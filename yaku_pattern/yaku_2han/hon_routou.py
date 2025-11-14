import const

# 混老頭判定関数
def check_hon_routou(situation_input):    
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in situation_input["hand_tiles"]:
        tiles_index.append(const.tiles[tile])

    # 中張牌が含まれる場合False
    if (not const.find_full_yaochu(tiles_index)):
        return False
    
    return True

import const

# 清老頭判定関数
def check_chin_routou(situation_input):    
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in situation_input["hand_tiles"]:
        tiles_index.append(const.tiles[tile])

    # 中張牌が含まれる場合False
    if (not const.find_full_yaochu(tiles_index)):
        return False
    
    # 字牌が含まれる場合False
    if any(index > 30 for index in tiles_index):
        return False
    
    return True

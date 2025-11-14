import const

ryu_iiso_tiles = (12, 13, 14, 16, 18, 36)

# 緑一色判定関数
def check_ryu_iiso(situation_input):    
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in situation_input["hand_tiles"]:
        tiles_index.append(const.tiles[tile])

    if any((index not in ryu_iiso_tiles) for index in tiles_index):
        # print("緑一色以外の牌が含まれています")
        return False
    
    return True
import const

# 清一色判定関数
def check_chin_iiso(situation_input):
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in situation_input["hand_tiles"]:
        tiles_index.append(const.tiles[tile])
    
    # 清一色でなければFalseを返す
    if (const.find_full_flush(tiles_index) != "清一色"):
        # print("清一色ではありませんでした")
        return False
    
    return True
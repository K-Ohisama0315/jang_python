import const

# 字一色判定関数
def check_tsu_iiso(hand_tiles, formed_calls) -> bool:
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in hand_tiles:
        tiles_index.append(const.tiles[tile])
    
    # 字一色でなければFalseを返す
    if (const.find_full_flush(tiles_index) != "字一色"):
        # print("字一色ではありませんでした")
        return False
    
    return True
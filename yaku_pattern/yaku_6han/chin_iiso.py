import const

# 清一色判定関数
def check_chin_iiso(hand_tiles, formed_calls) -> str:
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in hand_tiles:
        tiles_index.append(const.tiles[tile])
    
    for mentsu in formed_calls:
        for tile in mentsu:
            tiles_index.append(const.tiles[tile])

    # 清一色の判定
    if (const.find_full_flush(tiles_index) == "清一色"):
        # print("清一色でした")
        return "清一色"

    # 手牌から字牌を抜き出す
    honitsu_list = []
    for tile in honitsu_list:
        if tile < 30:
            honitsu_list.append(tile)

    # 混一色の判定
    if (const.find_full_flush(tiles_index) == "清一色"):
        return "混一色"

    return None
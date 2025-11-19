import const

ryu_iiso_tiles = (12, 13, 14, 16, 18, 36)

# 緑一色判定関数
def check_ryu_iiso_tsu_iiso(hand_tiles, formed_calls) -> str:    
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in hand_tiles:
        tiles_index.append(const.tiles[tile])
    
    for mentsu in formed_calls:
        for tile in mentsu:
            tiles_index.append(const.tiles[tile])

    # 字一色の場合リターン
    if (const.find_full_flush(tiles_index) == "字一色"):
        # print("字一色ではありませんでした")
        return "字一色"

    if any((index not in ryu_iiso_tiles) for index in tiles_index):
        # print("緑一色以外の牌が含まれています")
        return None
    
    return "緑一色"

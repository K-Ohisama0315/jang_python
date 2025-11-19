import collections

import const

# 七対子判定関数
def check_chiitoitsu(hand_tiles, menzen) -> bool:

    # 牌が14枚なければFalseを返す
    if (len(hand_tiles) != 14):
        return None

    # 面前でなければFalseを返す
    if (not menzen):
        # print("面前ではありませんでした")
        return False
    
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in hand_tiles:
        tiles_index.append(const.tiles[tile])
    
    work_counts = collections.Counter(tiles_index)

    if (not all(value == 2 for value in work_counts.values())):
        # print("対子ではない牌がありました")
        return False
    
    return True
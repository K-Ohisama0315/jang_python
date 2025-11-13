import collections

import const

# 七対子作成関数
def check_chiitoitsu(situation_input):
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in situation_input["hand_tiles"]:
        tiles_index.append(const.tiles[tile])

    # 面前でなければFalseを返す
    if (not situation_input["menzen"]):
        print("面前ではありませんでした")
        return False
    
    work_counts = collections.Counter(tiles_index)

    if (not all(value == 2 for value in work_counts.values())):
        print("対子ではない牌がありました")
        return False
    
    return True
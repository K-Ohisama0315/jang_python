import collections

import const

# 国士無双判定関数
def check_kokushi_musou(hand_tiles, menzen, agari_tile) -> str:

    # 牌が14枚なければFalseを返す
    if (len(hand_tiles) != 14):
        return None
    
    # 面前でなければFalseを返す
    if (not menzen):
        # print("面前ではありませんでした")
        return None
    
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in hand_tiles:
        tiles_index.append(const.tiles[tile])
    
    # 中張牌が含まれていればFalseを返す
    if (not const.find_full_yaochu(tiles_index)):
        # print("中張牌が含まれています")
        return None

    work_counts = collections.Counter(tiles_index)

    agari_index = const.tiles[agari_tile]
    junsei_work_counts = work_counts.copy()
    junsei_work_counts[agari_index] -= 1
    if (junsei_work_counts[agari_index] == 0):
        del junsei_work_counts[agari_index]
    
    if (len(junsei_work_counts) == 13):
        return "国士無双十三面待ち"

    if (len(work_counts) != 13):
        # print("足りない牌があります")
        return None
    
    return "国士無双"

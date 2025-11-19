import collections

import const

# 九蓮宝燈判定関数
def check_chuuren_poutou(hand_tiles, menzen, agari_tile) -> str:

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
    
    # 清一色でなければFalseを返す
    if (not (const.find_full_flush(tiles_index) != "清一色")):
        # print("清一色ではありませんでした")
        return None
    
    work_counts = collections.Counter(tiles_index)

    # 純正九蓮宝燈用にカウンタ変数を準備
    agari_index = const.tiles[agari_tile]
    junsei_work_counts = work_counts.copy()
    junsei_work_counts[agari_index] -= 1
    if (junsei_work_counts[agari_index] == 0):
        del junsei_work_counts[agari_index]

    # 純正九蓮宝燈判定
    if (len(junsei_work_counts) == 9):
        condition_1 = any(value >= 3 for key, value in junsei_work_counts.items() if key % 10 == 1)
        condition_9 = any(value >= 3 for key, value in junsei_work_counts.items() if key % 10 == 9)

        if  (condition_1 and condition_9):
             return "純正九蓮宝燈"


    if (len(work_counts) != 9):
        # print("牌が全種類ありませんでした")
        return None
    
    condition_1 = any(value >= 3 for key, value in work_counts.items() if key % 10 == 1)
    condition_9 = any(value >= 3 for key, value in work_counts.items() if key % 10 == 9)

    if not (condition_1 and condition_9):
        # print("1と9が3枚以上ありませんでした")
        return None

    return "九蓮宝燈"
# kokushimusou_pattern = ("1p", "9p", "1s", "9s", "1m", "9m",
#                     "east", "south", "west", "north", 
#                     "white", "green", "red")

# def check_kokushimusou(hands_set) -> bool:
#     """
#     手牌が国士無双かどうか判定する

#     :param:hand_set 手牌パターン
#     :return: bool
#     """
#     hands_pattern = hands_set["hand"]

#     # 国士無双のパターンに当てはまる牌を格納する空集合
#     kokushimusou_set = set()
    
#     # 手牌と国士無双の牌を照らし合わせるループ処理
#     for hand_tile in hands_pattern:
#         for kokushi_tile in kokushimusou_pattern:

#             # 手牌が国士無双のパターンに合う牌であれば、集合に代入する
#             if hand_tile == kokushi_tile:
#                 kokushimusou_set.add(hand_tile)
    
#     print(kokushimusou_set)

# hands_set = {"first":["1p", "2p", "9s", "8m", "east", "east"], "second":{"4p", "1s"}}
# check_kokushimusou(hands_set)

import collections

import const

# 国士無双判定関数
def check_kokushi_musou(situation_input):
    # 面前でなければFalseを返す
    if (not situation_input["menzen"]):
        print("面前ではありませんでした")
        return False
    
    tiles_index = []
    # 手牌を数値に置き換える
    for tile in situation_input["hand_tiles"]:
        tiles_index.append(const.tiles[tile])
    
    # 中張牌が含まれていればFalseを返す
    if (not const.find_full_yaochu(tiles_index)):
        print("中張牌が含まれています")
        return False

    work_counts = collections.Counter(tiles_index)

    agari_index = const.tiles[situation_input["agari_tile"]]
    junsei_work_counts = work_counts.copy()
    junsei_work_counts[agari_index] -= 1
    if (junsei_work_counts[agari_index] == 0):
        del junsei_work_counts[agari_index]
    
    if (len(junsei_work_counts) == 13):
        return "国士無双十三面待ち"

    if (len(work_counts) != 13):
        print("足りない牌があります")
        return False
    
    return "国士無双"

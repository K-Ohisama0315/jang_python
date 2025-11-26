from functools import lru_cache
import collections

import const
from yaku_pattern import *

                                                               
                                                                                          
#  ▄▄▄▄▄▄▄▄     ██                     ▄▄            ▄▄    ▄▄                            ▄▄ 
#  ██▀▀▀▀▀▀     ▀▀                     ██            ██    ██                            ██ 
#  ██         ████     ██▄████▄   ▄███▄██            ██    ██   ▄████▄    ▄█████▄   ▄███▄██ 
#  ███████      ██     ██▀   ██  ██▀  ▀██            ████████  ██▄▄▄▄██   ▀ ▄▄▄██  ██▀  ▀██ 
#  ██           ██     ██    ██  ██    ██            ██    ██  ██▀▀▀▀▀▀  ▄██▀▀▀██  ██    ██ 
#  ██        ▄▄▄██▄▄▄  ██    ██  ▀██▄▄███            ██    ██  ▀██▄▄▄▄█  ██▄▄▄███  ▀██▄▄███ 
#  ▀▀        ▀▀▀▀▀▀▀▀  ▀▀    ▀▀    ▀▀▀ ▀▀            ▀▀    ▀▀    ▀▀▀▀▀    ▀▀▀▀ ▀▀    ▀▀▀ ▀▀ 
                                                                                          
# 手牌の中から雀頭になりうる牌を取り出す
def find_head(hand_tiles):
    # 手牌を数値に変換
    tiles_index = []
    for tile in hand_tiles:
        tiles_index.append(const.tiles[tile])

    # 手牌の並び替え
    tiles_index.sort()

    # 雀頭になりうる牌を抽出し集合(set型)に格納
    head_index_set = set([])
    for i in range(len(tiles_index) - 1):
        if (tiles_index[i] == tiles_index[i + 1]):
            head_index_set.add(tiles_index[i])

    # 集合を配列に変換
    head_index = list(head_index_set)

    # 雀頭とそれ以外に分けて格納する
    a = []
    remove_count = 0
    for i, index in enumerate(head_index):
        works = tiles_index.copy()
        for _ in range(2):
            works.remove(index)
            remove_count += 1

        a.append({"work":works, "head":[index, index]})

    return a

                                                                                                              
#  ▄▄▄▄▄▄▄▄     ██                     ▄▄            ▄▄▄  ▄▄▄                                                   
#  ██▀▀▀▀▀▀     ▀▀                     ██            ███  ███                        ██                         
#  ██         ████     ██▄████▄   ▄███▄██            ████████   ▄████▄   ██▄████▄  ███████   ▄▄█████▄  ██    ██ 
#  ███████      ██     ██▀   ██  ██▀  ▀██            ██ ██ ██  ██▄▄▄▄██  ██▀   ██    ██      ██▄▄▄▄ ▀  ██    ██ 
#  ██           ██     ██    ██  ██    ██            ██ ▀▀ ██  ██▀▀▀▀▀▀  ██    ██    ██       ▀▀▀▀██▄  ██    ██ 
#  ██        ▄▄▄██▄▄▄  ██    ██  ▀██▄▄███            ██    ██  ▀██▄▄▄▄█  ██    ██    ██▄▄▄   █▄▄▄▄▄██  ██▄▄▄███ 
#  ▀▀        ▀▀▀▀▀▀▀▀  ▀▀    ▀▀    ▀▀▀ ▀▀            ▀▀    ▀▀    ▀▀▀▀▀   ▀▀    ▀▀     ▀▀▀▀    ▀▀▀▀▀▀    ▀▀▀▀ ▀▀ 
                                                                             
@lru_cache(None)
def find_all_mentsu(frozen_counts):

    counts = collections.Counter(dict(frozen_counts))
    if not counts:
        return [[]]

    results = []
    t = min(counts.keys())

    # 刻子探し
    if counts[t] >= 3:
        new_counts = counts.copy()
        # 刻子分を引く
        new_counts[t] -= 3
        # 牌がなくなった場合キーを消す
        if new_counts[t] == 0:
            del new_counts[t]
        
        # 再起処理
        sub_results = find_all_mentsu(frozenset(new_counts.items()))
        
        for r in sub_results:
            kotsu = [t, t, t]
            results.append([kotsu] + r)

    # 順子探し
    if t < 30 and t % 10 <= 7:
        if  t + 1 in counts and t + 2 in counts:
            new_counts = counts.copy()
            new_counts[t] -= 1
            new_counts[t + 1] -= 1
            new_counts[t + 2] -= 1

            if new_counts[t] == 0: del new_counts[t]
            if new_counts[t + 1] == 0: del new_counts[t + 1]
            if new_counts[t + 2] == 0: del new_counts[t + 2]

            sub_results = find_all_mentsu(frozenset(new_counts.items()))

            for r in sub_results:
                syuntsu = [t, t + 1, t + 2]
                results.append([syuntsu] + r)
    return results

                                                                                          
#  ▄▄▄▄▄▄▄▄     ██                     ▄▄           ▄▄      ▄▄              ██              
#  ██▀▀▀▀▀▀     ▀▀                     ██           ██      ██              ▀▀       ██     
#  ██         ████     ██▄████▄   ▄███▄██           ▀█▄ ██ ▄█▀  ▄█████▄   ████     ███████  
#  ███████      ██     ██▀   ██  ██▀  ▀██            ██ ██ ██   ▀ ▄▄▄██     ██       ██     
#  ██           ██     ██    ██  ██    ██            ███▀▀███  ▄██▀▀▀██     ██       ██     
#  ██        ▄▄▄██▄▄▄  ██    ██  ▀██▄▄███            ███  ███  ██▄▄▄███  ▄▄▄██▄▄▄    ██▄▄▄  
#  ▀▀        ▀▀▀▀▀▀▀▀  ▀▀    ▀▀    ▀▀▀ ▀▀            ▀▀▀  ▀▀▀   ▀▀▀▀ ▀▀  ▀▀▀▀▀▀▀▀     ▀▀▀▀  
                                                                                          
# 待ち方を全通り調べる
def find_wait(agari_dict, agari_tile):
    # 手牌を数値に置き換える
    hand_num = const.change_hand_to_num(agari_dict["hand"])
    head_tiles = []
    for tile in agari_dict["head"]:
        head_tiles.append(const.tiles[tile])
    hand_num.append(head_tiles)
    agari_tile_num = const.tiles[agari_tile]

    # 待ち方を集合に格納していく
    wait_set = set()
    for mentsu in hand_num:
        if (agari_tile_num not in mentsu):  # 面子にアガリ牌が含まれていない場合スキップ
            continue

        if (len(mentsu) == 2):      # 単騎待ちのとき
            wait_set.add("tanki")
            continue

        if (len(set(mentsu)) == 1): # 双ポン待ちのとき
            wait_set.add("shanpon")
            continue

        if (min(mentsu) < agari_tile_num < max(mentsu)):    # 嵌張待ちのとき
            wait_set.add("kanchan")  
        else:
            # 辺張待ちの条件
            is_penchan = (agari_tile_num % 10 == 3 and agari_tile_num == max(mentsu)) or \
                         (agari_tile_num % 10 == 7 and agari_tile_num == min(mentsu))
            if (is_penchan):    # 辺張待ちのとき
                wait_set.add("penchan")
            else:               # 両面待ちのとき
                wait_set.add("ryanmen")
    
    wait_tuple = tuple(wait_set)

    agari_dict_list = []
    for wait in wait_tuple:
        agari_dict["wait"] = wait
        agari_dict_list.append(agari_dict.copy())
    
    return agari_dict_list

#  ▄▄▄  ▄▄▄               ██              
#  ███  ███               ▀▀              
#  ████████   ▄█████▄   ████     ██▄████▄ 
#  ██ ██ ██   ▀ ▄▄▄██     ██     ██▀   ██ 
#  ██ ▀▀ ██  ▄██▀▀▀██     ██     ██    ██ 
#  ██    ██  ██▄▄▄███  ▄▄▄██▄▄▄  ██    ██ 
#  ▀▀    ▀▀   ▀▀▀▀ ▀▀  ▀▀▀▀▀▀▀▀  ▀▀    ▀▀ 
def main_agari_process(situation_input):

    final_agari_list = []
    # 九蓮宝燈形かどうかの判定
    yaku_chuuren = check_chuuren_poutou(situation_input["hand_tiles"], situation_input["menzen"], situation_input["agari_tile"])
    if (not yaku_chuuren == None):
        situation_input["formed_hands"].append({"hand":[situation_input["hand_tiles"]], "head":[], "wait":[]})
        return yaku_chuuren
    
    # 国士無双形かどうかの判定
    yaku_kokuchi = check_kokushi_musou(situation_input["hand_tiles"], situation_input["menzen"], situation_input["agari_tile"])
    if (not yaku_kokuchi == None):
        situation_input["formed_hands"].append({"hand":[situation_input["hand_tiles"]], "head":[], "wait":[]})
        return yaku_kokuchi
    
    # 七対子形かどうかの判定
    yaku_chiitoitsu = check_chiitoitsu(situation_input["hand_tiles"], situation_input["menzen"])
    if (yaku_chiitoitsu):
        final_agari_list.append({"hand":[situation_input["hand_tiles"]], "head":[], "wait":[]})

    # 手牌の中から雀頭になりうる牌を取り出す
    hand_head = find_head(situation_input["hand_tiles"])

    unique_all_mentsu_set = set()
    for i, hand in enumerate(hand_head):
        # 牌をカウントのタプルに置き換える(1pが3つなら、"1p":3 みたいなイメージ)
        work_counts = collections.Counter(hand["work"])

        # アガリの重複削除
        all_mentsu_list = (find_all_mentsu(frozenset(work_counts.items())))
        for mentsu_list in all_mentsu_list:
            tuple_mentsu = [tuple(m) for m in mentsu_list]
            tuple_mentsu.sort()

            full_tuple_mentsu = (tuple(tuple_mentsu), tuple(hand["head"]))
            unique_all_mentsu_set.add(full_tuple_mentsu)

    agari_dict_list = []
    for agari_tuple in unique_all_mentsu_set:
        # タプルをリストに戻し、文字に変換する
        agari_list = ([[const.tiles_swap[num] for num in list(m)] for m in agari_tuple[0]]), \
                      ([const.tiles_swap[num] for num in list(agari_tuple[1])])

        agari_dict = {y: x for y, x in zip((["hand", "head"]), agari_list)}
        
        # 待ち方を格納する関数を呼び出す
        agari_dict_list = find_wait(agari_dict, situation_input["agari_tile"])
        
        # 暗槓を手牌に追加する
        
        for call_tiles in situation_input["call_tiles"]:
            if (call_tiles["calling"] == "an_kan"):
                for an_kan_tiles in call_tiles["mentsu"]:
                    agari_dict_list[0]["hand"].append(an_kan_tiles)
            else:
                    for an_kan_tiles in call_tiles["mentsu"]:
                        situation_input["formed_calls"].append(an_kan_tiles)
    
    final_agari_list.append(agari_dict_list.copy())            

    situation_input["formed_hands"] = final_agari_list

        
    

from functools import lru_cache
import collections

import const
from yaku_pattern import *

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


def main_agari_process(situation_input):

    final_agari_list = []
    yaku_chuuren = check_chuuren(situation_input)
    if (not yaku_chuuren == None):
        final_agari_list = {"hand":situation_input["hand_tiles"], "head":[]}
        situation_input["formed_hands"] = final_agari_list
        return yaku_chuuren
    
    yaku_kokuchi = check_kokushi_musou(situation_input)
    if (not yaku_kokuchi == None):
        final_agari_list = {"hand":situation_input["hand_tiles"], "head":[]}
        situation_input["formed_hands"] = final_agari_list
        return yaku_kokuchi
    
    yaku_chiitoitsu = check_chiitoitsu(situation_input)
    if (yaku_chiitoitsu):
        final_agari_list.append({"hand":situation_input["hand_tiles"], "head":[]})

    # 手牌の中から雀頭になりうる牌を取り出す
    hand_head = find_head(situation_input["hand_tiles"])

    all_agari = []
    unique_all_mentsu_set = set()
    for i, hand in enumerate(hand_head):
        # 牌をカウントのタプルに置き換える(1pが3つなら、"1p":3 みたいなイメージ)
        work_counts = collections.Counter(hand["work"])

        # アガリの重複削除
        all_mentsu_list = (find_all_mentsu(frozenset(work_counts.items())))
        for mentsu_list in all_mentsu_list:
            if len(mentsu_list) == 4:
                tuple_mentsu = [tuple(m) for m in mentsu_list]
                tuple_mentsu.sort()

                full_tuple_mentsu = (tuple(tuple_mentsu), tuple(hand["head"]))
                unique_all_mentsu_set.add(full_tuple_mentsu)

    for agari_tuple in unique_all_mentsu_set:
        # タプルをリストに戻し、文字に変換する
        agari_list = ([[const.tiles_swap[num] for num in list(m)] for m in agari_tuple[0]]), ([const.tiles_swap[num] for num in list(agari_tuple[1])])

        agari_dict_str = {y: x for y, x in zip((["hand", "head"]), agari_list)}
        final_agari_list.append(agari_dict_str)

    situation_input["formed_hands"] = final_agari_list

        


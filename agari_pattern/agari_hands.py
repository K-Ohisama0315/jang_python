from functools import lru_cache
import collections

import const

# 手牌の中から雀頭になりうる牌を取り出す
def find_head(hand_tiles):
    # 手牌を数値に変換
    tiles_index = []
    for tile in hand_tiles:
        tiles_index.append(const.tiles[tile])

    # 手牌の並び替え
    tiles_index.sort()
    print(tiles_index)

    # 雀頭になりうる牌を抽出し集合(set型)に格納
    head_index_set = set([])
    for i in range(len(tiles_index) - 1):
        if (tiles_index[i] == tiles_index[i + 1]):
            head_index_set.add(tiles_index[i])

    # 集合を配列に変換
    head_index = list(head_index_set)
    print("head_index", head_index)

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


def find_all_mentsu(counts):

    if not counts:
        return [[]]

    results = []
    t = min(counts.keys())
    print(t)

    # 刻子探し
    if counts[t] >= 3:
        new_counts = counts.copy()
        # 刻子分を引く
        new_counts[t] -= 3
        # 牌がなくなった場合キーを消す
        if new_counts[t] == 0:
            del new_counts[t]
        
        # 再起処理
        sub_results = find_all_mentsu(new_counts)
        
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

            sub_results = find_all_mentsu(new_counts)

            for r in sub_results:
                syuntsu = [t, t + 1, t + 2]
                results.append([syuntsu] + r)
    print(results)
    return results

def main_agari_process(hand_tiles):
    # 手牌の中から雀頭になりうる牌を取り出す
    hand_head = find_head(hand_tiles["hand"])

    mentsu = []
    for hand in hand_head:
        print("main:", hand)
        work_counts = collections.Counter(hand["work"])
        mentsu.append(find_all_mentsu(work_counts))
    
    for a in mentsu:
        for b in a:
            print("mentsu",b)
        


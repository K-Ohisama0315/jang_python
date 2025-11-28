tiles = {
    "1p":1, "2p":2, "3p":3, "4p":4, "5p":5, "6p":6, "7p":7, "8p":8, "9p":9, 
    "1s":11, "2s":12, "3s":13, "4s":14, "5s":15, "6s":16, "7s":17, "8s":18, "9s":19, 
    "1m":21, "2m":22, "3m":23, "4m":24, "5m":25, "6m":26, "7m":27, "8m":28, "9m":29, 
    "east":31, "south":32, "west":33, "north":34, "white":35, "green":36, "red":37, 
}
tiles_swap = {v: k for k, v in tiles.items()}

yaku_han = {
    "平和":1,"断么九":1,"役牌：自風牌":1,"役牌：場風牌":1,"役牌：白":1,"役牌：發":1,"役牌：中":1,"平和":1,"一盃口":1,
    "三色同刻":2,"三槓子":2,"対々和":2,"三暗刻":2,"小三元":2,"混老頭":2,"七対子":2,"混全帯么九":2,"一気通貫":2,"三色同順":2,
    "二盃口":3,"純全帯么九":3,"混一色":3,  "清一色":6
}
kuisagari = ("一気通貫", "三色同順", "混全帯么九", "純全帯么九", "混一色", "清一色")

yaku_sort = [
    "立直","ダブル立直","一発","嶺上開花","槍槓","門前清自摸和","海底摸月","河底撈魚","平和","断么九",
    "一盃口","役牌：自風牌","役牌：場風牌","役牌：白","役牌：發","役牌：中",
    "対々和","三暗刻","小三元","混老頭","三槓子","三色同順","三色同刻","七対子","混全帯幺九","一気通貫",
    "二盃口","純全帯幺九","混一色","清一色",
    "清老頭","大三元","字一色","緑一色","四槓子","四暗刻","小四喜","国士無双","九蓮宝燈",
    "四暗刻単騎待ち","大四喜","国士無双十三面待ち","純正九蓮宝燈"
]


# 清一色であるかの判定を行う
def find_full_flush(tiles_index):
    for index in tiles_index:
        # 一色では無ければリターン
        if (index // 10 != tiles_index[0] // 10): 
            return None
        
    for index in tiles_index:
        # 字牌が存在すればリターン
        if (index > 30): 
            return "字一色"
    
    return "清一色"

# すべて么九牌かどうかの判定を行う
def find_full_yaochu(tiles_index):
    for index in tiles_index:
        # 中張牌はFalse
        if (index < 30 and (index % 10 not in (1,9))):
            return False
    
    return True

# 手牌の情報を数値に変換する関数
def change_hand_to_num(hand) -> list:

    numbered_hand = []  # 戻り値を格納するリスト

    for mentsu in hand:
        mentsu_num = [] # 数値に変換した牌の情報を格納するリスト

        for tile in mentsu:

            tile_num = tiles[tile]    # 数値に変換
            mentsu_num.append(tile_num)

        numbered_hand.append(mentsu_num)
    
    return numbered_hand

# 順子であるか判定する関数(面子の情報が数値に変換されていることが前提の関数)
def find_shuntsu(mentsu) -> bool:

    for tile in mentsu:
        if tile > 30:   # 字牌が含まれている場合
            return False

    # 隣り合う要素の差が１であれば順子と判定する
    if mentsu[0] + 1 == mentsu[1] and mentsu[1] + 1 == mentsu[2]:
        return True

    else:
        return False
    



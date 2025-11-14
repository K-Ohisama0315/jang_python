from enum import Enum

tiles = {
    "1p":1, "2p":2, "3p":3, "4p":4, "5p":5, "6p":6, "7p":7, "8p":8, "9p":9, 
    "1s":11, "2s":12, "3s":13, "4s":14, "5s":15, "6s":16, "7s":17, "8s":18, "9s":19, 
    "1m":21, "2m":22, "3m":23, "4m":24, "5m":25, "6m":26, "7m":27, "8m":28, "9m":29, 
    "east":31, "south":32, "west":33, "north":34, "white":35, "green":36, "red":37, 
}

tiles_swap = {v: k for k, v in tiles.items()}

# 清一色であるかの判定を行う
def find_full_flush(tiles_index):
    for index in tiles_index:
        # 一色では無ければリターン
        if (index // 10 != tiles_index[0] // 10): 
            return None
        
    # 先頭が字牌なら字一色
    if (tiles_index[0] > 30):
        return "字一色"
    
    return "清一色"

# すべて么九牌かどうかの判定を行う
def find_full_yaochu(tiles_index):

    # 中張牌が含まれる場合はFalse
    if any((index < 30 and (index % 10 not in (1,9))) for index in tiles_index):
        return False
    
    return True
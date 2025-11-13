kaze_tile = ["east", "south", "west", "north"]

def check_daisuushi(formed_hand, call_tile) -> str:
    """
    大四喜が成立するか判定する
    """
    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in call_tile:
        hand.append(mentsu)

    # 刻子を抽出する
    kotsu = []
    for mentsu in hand:
        if mentsu[0] == mentsu[1] == mentsu[2]:
            kotsu.append(mentsu)
    
    # 刻子の中に風牌があれば集合に追加
    kaze_set = set()
    for tile in kotsu:
        if tile[0] in kaze_tile:
            kaze_set.add(tile[0])
    
    # 風牌の集合の要素数が4であれば大四喜成立
    if len(kaze_set) == 4:
        return "daisuushi"
    
    # 風牌の集合の要素数が3の時
    if len(kaze_set) == 3:
        head = formed_hand["head"]
        # アタマが風牌であれば小四喜成立 
        if head[0] in kaze_tile and head[0] not in kaze_set:
            return "shousuushi"
    
    # それ以外は不成立
    return None

hand_set = {"hand":[["2s","3s","3s"],["west","west","west"],["1s","1s","1s"]],"head":["north","north"]}
call_tile = [["east","east","east"],]
print(check_daisuushi(hand_set, call_tile))
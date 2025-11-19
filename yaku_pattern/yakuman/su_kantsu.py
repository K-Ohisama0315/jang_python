# 四槓子、三槓子判定関数
def check_su_kantsu(formed_hand, formed_call) -> str:

    hand = formed_hand["hand"]

    # 副露牌を手牌に追加
    for mentsu in formed_call:
        hand.append(mentsu)
    
    # 槓子がいくつあるかカウントする
    kantsu_count = 0
    for mentsu in hand:
        tile_count = 0
        for tile in mentsu:
            if mentsu[0] == tile:
                tile_count += 1
        if tile_count == 4:
            kantsu_count += 1
    
    # 槓子が4つ存在する場合
    if kantsu_count == 4:
        return "四槓子"
    
    # 槓子が3つ存在する場合
    if kantsu_count == 3:
        return "三槓子"
    
    # 槓子が2つ以下の場合
    return None

formed_hand = {"hand":[["3m","3m","3m","3m"],["6p","6p","6p","6p"]],"head":["8m","8m"]}
formed_call = [["2m","2m","2m","2m"],["5s","5s","5s","5s"]]
print(check_su_kantsu(formed_hand, formed_call))
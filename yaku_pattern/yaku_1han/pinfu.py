import const

yakuhai = ["white", "green", "red"]

def check_pinfu(menzen, bakaze, zikaze, agari_tile, formed_hand) -> bool:
    """
    平和が成立するか判定する
    """
    
    # 面前であるか判定する
    if not menzen:
        return False
    
    # 役牌リストに場風・自風を追加する
    yakuhai.append(bakaze)
    yakuhai.append(zikaze)
    
    # 頭が役牌でないか判定する
    head = formed_hand["head"]
    for tile in head:
        if tile in yakuhai:
            return False
    
    # 手牌がすべて順子で構成されているか判定する
    hand = formed_hand["hand"]

    mentsu_hand = []
    for mentsu in hand:
        num_mentsu = []

        for tile in mentsu: # 手牌を数値に変換する
            num = const.tiles[tile]
            if num >= 30:  # 字牌が含まれている場合、Falseを返す
                return False
            num_mentsu.append(num)

        mentsu_hand.append(num_mentsu)

    shuntsu_hand = []
    for mentsu in mentsu_hand:  # 順子であるか判定する
        if (mentsu[0] + 1 == mentsu[1] and mentsu[1] + 1 == mentsu[2]):
            shuntsu_hand.append(mentsu)

    
    if len(shuntsu_hand) < 4:   # 順子が４組未満の場合、Falseを返す
        return False
        
    # 待ちが両面待ちであるか判定する
    agari_num = const.tiles[agari_tile]  # アガリ牌の数字部分を抽出
    for tile in mentsu_hand:
        mentsu_set = set()
        mentsu_set = {tile[0] % 10, tile[1] % 10, tile[2] % 10} # 末尾の数字のみを抽出して集合に格納

        if 1 in mentsu_set or 9 in mentsu_set:  # 1か9が面子に含まれている場合
            if agari_num % 10 == 1 or agari_num % 10 == 9:
                return True
        
        else:   # 么九牌だけで面子が構成されている場合
            if agari_num == tile[0] or agari_num == tile[2]:
                return True
    
    return False

menzen = True
bakaze = "east"
zikaze = "south"
agari_tile = "west"
hand_set = {"hand":[["1m","2m","3m"],["4m","5m","6m"],["7m","8m","9m"],["1s","2s","3s"]],"head":["west","west"]}
print(check_pinfu(menzen, bakaze, zikaze, agari_tile, hand_set))
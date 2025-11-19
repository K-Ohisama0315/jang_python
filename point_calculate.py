import helper

from yaku_pattern import *

                                                                      
#     ▄▄▄▄                                           ▄▄▄▄               
#    ██▀▀▀                                           ▀▀██               
#  ███████   ██    ██             ▄█████▄   ▄█████▄    ██       ▄█████▄ 
#    ██      ██    ██            ██▀    ▀   ▀ ▄▄▄██    ██      ██▀    ▀ 
#    ██      ██    ██            ██        ▄██▀▀▀██    ██      ██       
#    ██      ██▄▄▄███            ▀██▄▄▄▄█  ██▄▄▄███    ██▄▄▄   ▀██▄▄▄▄█ 
#    ▀▀       ▀▀▀▀ ▀▀              ▀▀▀▀▀    ▀▀▀▀ ▀▀     ▀▀▀▀     ▀▀▀▀▀  
#                     ▀▀▀▀▀▀▀▀▀▀                                        
def fu_calc(formed_hand, situation_input, yaku_set):
    # 基礎点
    fu = 20

    # 平和判定用変数
    is_pinfu = True

    # 面子の形によるボーナス(手牌)
    for mentsu in formed_hand["hand"]:
        if (len(mentsu) == 14):
            if (check_chiitoitsu(mentsu, situation_input["menzen"])):
                fu = 25
                return fu
            else:
                fu = 0
            return fu
        
        # 牌を集合に入れる
        mentsu_set = set(mentsu)
        # 順子はスキップ
        if (len(mentsu_set) != 1):
            continue

        # 暗槓や暗刻があるため平和は成立しない
        is_pinfu = False

        tile = mentsu_set[0]
        # 么九牌用に倍率設定
        yaochu_bonus = 1 if (tile < 30 and tile % 10 not in (1, 9)) else 2

        # 暗槓の場合は16符、暗刻の場合は4符追加(么九牌は2倍)
        fu += 16 * yaochu_bonus if (len(mentsu) == 4) else 4 * yaochu_bonus

    # 面子の形によるボーナス(鳴き牌)
    for mentsu in situation_input["formed_calls"]:

        # 鳴き牌があるため平和は成立しない
        is_pinfu = False

        # 牌を集合に入れる
        mentsu_set = set(mentsu)
        # 順子はスキップ
        if (len(mentsu_set) != 1):
            continue

        tile = mentsu_set[0]
        # 么九牌用に倍率設定
        yaochu_bonus = 1 if (tile < 30 and tile % 10 not in (1, 9)) else 2

        # 明槓の場合は8符、明刻の場合は2符追加(么九牌は2倍)
        fu += 8 * yaochu_bonus if (len(mentsu) == 4) else 2 * yaochu_bonus

    # 雀頭が役牌の場合
    if (set(formed_hand["head"])[0] > 30):
        # 平和は成立しない
        is_pinfu = False

        # 2符追加
        fu += 2 

    # 単騎待ち、嵌張待ち、辺張待ちの場合
    if formed_hand["wait"] in ("tanki", "kanchan", "penchan"):
        # 平和は成立しない
        is_pinfu = False

        # 2符追加
        fu += 2 

    # 門前ロンの場合
    if situation_input["menzen"] and situation_input["agari_situation"] == "ron":
        # 10符追加
        fu += 10

    # ツモの場合
    if situation_input["agari_situation"] == "tsumo":
        # 2符追加
        fu += 2

        # 平和ツモは20符固定
        if (is_pinfu):
            fu = 20

    if (is_pinfu):
        yaku_set.add("平和")

    #1の位を切り上げた符を返す
    return helper.ceil(fu, 1)
                                                                                
#  ▄▄                                                          ▄▄▄▄               
#  ██                                                          ▀▀██               
#  ██▄████▄   ▄█████▄  ██▄████▄             ▄█████▄   ▄█████▄    ██       ▄█████▄ 
#  ██▀   ██   ▀ ▄▄▄██  ██▀   ██            ██▀    ▀   ▀ ▄▄▄██    ██      ██▀    ▀ 
#  ██    ██  ▄██▀▀▀██  ██    ██            ██        ▄██▀▀▀██    ██      ██       
#  ██    ██  ██▄▄▄███  ██    ██            ▀██▄▄▄▄█  ██▄▄▄███    ██▄▄▄   ▀██▄▄▄▄█ 
#  ▀▀    ▀▀   ▀▀▀▀ ▀▀  ▀▀    ▀▀              ▀▀▀▀▀    ▀▀▀▀ ▀▀     ▀▀▀▀     ▀▀▀▀▀  
#                               ▀▀▀▀▀▀▀▀▀▀                                        
def han_calc(formed_hand, situation_input):
    pass

def point_calculateing (situation_input):
    
    """
    麻雀の点数を計算する関数
    """
    # 翻、符を0で初期化する
    han = 0
    fu = 0

    # 役集合の宣言
    yaku_set = set()

    jikaze = situation_input["jikaze"]
    bakaze = situation_input["bakaze"]
    agari_tile = situation_input["agari_input"]

    formed_hands = situation_input["formed_hand"]
    call_tiles = situation_input["call_tiles"]

    # 立直している場合
    if situation_input["riichi"] == 2:
        han += 2
        yaku_set.add("ダブル立直")
    elif situation_input["riichi"] == 1:
        han += 1
        yaku_set.add("立直")

    # 面前清自摸和の場合
    if situation_input["menzen"] and situation_input["agari_situation"] == "ツモ":
        han += 1
        yaku_set.add("面前清自摸和")
    
    # 槍槓の場合
    if situation_input["chankan"]:
        han += 1
        yaku_set.add("槍槓")

    # 嶺上開花の場合
    if situation_input["rinshan"]:
        han += 1
        yaku_set.add("嶺上開花")

    # 海底摸月の場合
    if situation_input["last_tsumo"] and situation_input["agari_situation"] == "tsumo":
        han += 1
        yaku_set.add("海底摸月")

    # 河底撈魚の場合
    if situation_input["last_tsumo"] and situation_input["agari_situation"] == "ron":
        han += 1
        yaku_set.add("海底摸月")

    # 一発の場合
    if situation_input["ippatsu"]:
        han += 1
        yaku_set.add("一発")

    # ドラの計算
    for dora_tile in situation_input["display_dora_tiles"]:
        for hand_tile in situation_input["hand_tiles"]:
            if dora_tile == hand_tile:
                han += 1
    
    if han > 1:
        yaku_set.add("ドラ", han)

    for formed_hand in formed_hands:
        # 符計算
        fu += fu_calc(formed_hand, situation_input, yaku_set)
        
        # 翻計算
        han += han_calc(formed_hand, situation_input)
     
    # 基本点の計算
    # 役満の場合
    # if yakuman_type == '役満':
    #     if host:
    #         if agari == 'ツモ':
    #             result = {'合計':48000, '子': 16000}

    #         elif agari == 'ロン':
    #             result = {'合計':48000}

    #     else:
    #         if agari == 'ツモ':
    #             result = {'合計':32000, '親':16000, '子': 8000}
                
    #         elif agari == 'ロン':
    #             result = {'合計':32000}

    #     return result
            
    # 役満以外の場合
    basic_point = 0

    if han >= 13:   # 数え役満
        basic_point = 8000

    elif han >= 11: # 三倍満
        basic_point = 6000
    
    elif han >= 8:  # 倍満
        basic_point = 4000
    
    elif han >= 6:  # 跳満
        basic_point = 3000
    
    elif han >= 5:  # 満貫
        basic_point = 2000
    
    else:
        basic_point = (2 ** (han + 2)) * fu

        if basic_point > 2000:  # 満貫以下で基本点が2000点を超えた場合
            basic_point = 2000
    
    # 満貫未満の基本点切り上げ
    if han < 5 and basic_point < 2000:
        basic_point = helper.ceil(basic_point, 3)
    
    # 最終的な点数の計算
    if situation_input["agari_situation"] == "ツモ":
        payment = helper.ceil(basic_point, 3)
        result = {"親":{'合計':payment*6, '子':payment*2}, "子":{'合計':payment*4, '親':payment*2, '子':payment}}
    
    elif situation_input["agari_situation"] == "ロン":
        payment = helper.ceil(basic_point, 3)
        result = {"親":{'合計':payment*6}, "子":{'合計':payment*4}}
    
    return result
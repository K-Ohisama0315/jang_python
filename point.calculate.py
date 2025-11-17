import helper

from yaku_pattern import *

def point_calculateing (sitiation_input):
    
    """
    麻雀の点数を計算する関数
    """
    # 翻、符を0で初期化する
    han = 0
    hu = 0

    # 役集合の宣言
    yaku_set = set()

    jikaze = sitiation_input["jikaze"]
    bakaze = sitiation_input["bakaze"]
    agari_tile = sitiation_input["agari_input"]

    formed_hands = sitiation_input["formed_hand"]
    call_tiles = sitiation_input["call_tiles"]

    # 立直している場合
    if sitiation_input["riichi"] == 2:
        han += 2
        yaku_set.add("ダブル立直")
    elif sitiation_input["riichi"] == 1:
        han += 1
        yaku_set.add("立直")

    # 面前清自摸和の場合
    if sitiation_input["menzen"] and sitiation_input["agari_situation"] == "ツモ":
        han += 1
        yaku_set.add("面前清自摸和")
    
    # 槍槓の場合
    if sitiation_input["chankan"]:
        han += 1
        yaku_set.add("槍槓")

    # 嶺上開花の場合
    if sitiation_input["rinshan"]:
        han += 1
        yaku_set.add("嶺上開花")

    # 海底摸月の場合
    if sitiation_input["last_tsumo"] and sitiation_input["agari_situation"] == "tsumo":
        han += 1
        yaku_set.add("海底摸月")

    # 河底撈魚の場合
    if sitiation_input["last_tsumo"] and sitiation_input["agari_situation"] == "ron":
        han += 1
        yaku_set.add("海底摸月")

    # 一発の場合
    if sitiation_input["ippatsu"]:
        han += 1
        yaku_set.add("一発")

    # ドラの計算
    for dora_tile in sitiation_input["display_dora_tiles"]:
        for hand_tile in sitiation_input["hand_tiles"]:
            if dora_tile == hand_tile:
                han += 1
    
    if han > 1:
        yaku_set.add("ドラ", han)

    for formed_hand in formed_hands:
        print()
        # 符計算
     
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
    
    elif (han >= 4 and hu >= 40) or (han >= 3 and hu >= 70):
        basic_point = 2000
    
    else:
        basic_point = (2 ** (han + 2)) * hu

        if basic_point > 2000:  # 満貫以下で基本点が2000点を超えた場合
            basic_point = 2000
    
    # 満貫未満の基本点切り上げ
    if han < 5 and basic_point < 2000:
        basic_point = helper.ceil(basic_point, 3)
    
    # 最終的な点数の計算
    if sitiation_input["agari_situation"] == "ツモ":
        payment = helper.ceil(basic_point, 3)
        result = {"親":{'合計':payment*6, '子':payment*2}, "子":{'合計':payment*4, '親':payment*2, '子':payment}}
    
    elif sitiation_input["agari_situation"] == "ロン":
        payment = helper.ceil(basic_point, 3)
        result = {"親":{'合計':payment*6}, "子":{'合計':payment*4}}
    
    return result
import helper

def point_calculateing (han, hu, agari, host=False, yakuman_type=None):
    
    """
    麻雀の点数を計算する関数

    :param han: 翻数
    :param hu: 符数
    :param agari: ツモかロン
    :param host: 親か子
    :oaram yakuman_type: 役満の種類
    """
     
    # 基本点の計算
    # 役満の場合
    if yakuman_type == '役満':
        if host:
            if agari == 'ツモ':
                result = {'合計':48000, '子': 16000}

            elif agari == 'ロン':
                result = {'合計':48000}

        else:
            if agari == 'ツモ':
                result = {'合計':32000, '親':16000, '子': 8000}
                
            elif agari == 'ロン':
                result = {'合計':32000}

        return result
            
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
    if host:
        if agari == "ツモ":
            payment = helper.ceil(basic_point, 3)
            result = {'合計':payment*6, '子':payment*2}
        
        elif agari == "ロン":
            payment = helper.ceil(basic_point, 3)
            result = {'合計':payment*6}
    
    else:
        if agari == "ツモ":
            payment = helper.ceil(basic_point, 3)
            result = {'合計':payment*4, '親':payment*2, '子':payment}
        
        elif agari == "ロン":
            payment = helper.ceil(basic_point, 3)
            result = {'合計':payment*4}
    
    return result

print(point_calculateing(han=5, hu=30, agari="ロン", host=True, yakuman_type="役満"))
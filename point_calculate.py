import jaconv
import sys

import helper
import const
from yaku_pattern import *

# 数値を漢数字に置き換える(二倍役満とかに使う)
num_to_kanji = str.maketrans({
    '0': '〇', '1': '一', '2': '二', '3': '三', '4': '四',
    '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'
})

                                                                      
#     ▄▄▄▄                                           ▄▄▄▄               
#    ██▀▀▀                                           ▀▀██               
#  ███████   ██    ██             ▄█████▄   ▄█████▄    ██       ▄█████▄ 
#    ██      ██    ██            ██▀    ▀   ▀ ▄▄▄██    ██      ██▀    ▀ 
#    ██      ██    ██            ██        ▄██▀▀▀██    ██      ██       
#    ██      ██▄▄▄███            ▀██▄▄▄▄█  ██▄▄▄███    ██▄▄▄   ▀██▄▄▄▄█ 
#    ▀▀       ▀▀▀▀ ▀▀              ▀▀▀▀▀    ▀▀▀▀ ▀▀     ▀▀▀▀     ▀▀▀▀▀  
#                     ▀▀▀▀▀▀▀▀▀▀                                       
# 符計算関数 
def fu_calc(formed_hand, situation_input, yaku_set, calc_dict) -> int:
    # 基礎点
    calc_dict["fu"] = 20

    # 平和判定用変数
    is_pinfu = True

    # 先頭行に牌が14枚ある場合は特殊アガリ(国士無双、九蓮宝燈、七対子)なのでリターン
    if (len(formed_hand["hand"][0]) == 14):
        # 七対子は25符固定
        if (check_chiitoitsu(formed_hand["hand"][0], situation_input["menzen"])):
            calc_dict["fu"] = 25
            return
        # 国士無双、九蓮宝燈は符計算が必要ない
        else:
            calc_dict["fu"] = 0
        return

    # 面子の形によるボーナス(手牌)
    for mentsu in formed_hand["hand"]:
        
        # 牌を集合に入れる
        mentsu_set = set(mentsu)
        # 順子はスキップ
        if (len(mentsu_set) != 1):
            continue

        # 暗槓や暗刻があるため平和は成立しない
        is_pinfu = False

        tile_str = next(iter(mentsu_set))
        # シャンポン待ちのロンは符計算では明刻扱い
        if (tile_str == situation_input["agari_tile"] and formed_hand["wait"] == "shanpon"):
            fu_work = 2
        elif (len(mentsu) == 3):    # 暗刻
            fu_work = 4
        elif (len(mentsu) == 4):    # 暗槓
            fu_work = 16
        else:
            print("符計算のエラー(暗刻・暗槓)")
            return

        tile = const.tiles[tile_str]

        # 么九牌用に倍率設定
        yaochu_bonus = 1 if (tile < 30 and tile % 10 not in (1, 9)) else 2

        # 暗槓の場合は16符、暗刻の場合は4符追加(么九牌は2倍)
        calc_dict["fu"] += fu_work * yaochu_bonus

    # 面子の形によるボーナス(鳴き牌)
    for mentsu in situation_input["formed_calls"]:

        # 鳴き牌があるため平和は成立しない
        is_pinfu = False

        # 牌を集合に入れる
        mentsu_set = set(mentsu)
        # 順子はスキップ
        if (len(mentsu_set) != 1):
            continue

        tile_str = next(iter(mentsu_set))
        if (len(mentsu) == 3):      # 明刻
            fu_work = 2
        elif (len(mentsu) == 4):    # 明槓
            fu_work = 8
        else:
            print("符計算のエラー(明刻・明槓)")
            return

        tile = const.tiles[tile_str]

        # 么九牌用に倍率設定
        yaochu_bonus = 1 if (tile < 30 and tile % 10 not in (1, 9)) else 2

        # 明槓の場合は8符、明刻の場合は2符追加(么九牌は2倍)
        calc_dict["fu"] += fu_work * yaochu_bonus

    # 雀頭が役牌の場合
    if (formed_hand["head"][0] in ("white", "green", "red", situation_input["jikaze"], situation_input["bakaze"])):
        # 平和は成立しない
        is_pinfu = False

        # 2符追加
        calc_dict["fu"] += 2 

    # 単騎待ち、嵌張待ち、辺張待ちの場合
    if formed_hand["wait"] in ("tanki", "kanchan", "penchan"):
        # 平和は成立しない
        is_pinfu = False

        # 2符追加
        calc_dict["fu"] += 2 

    # 門前ロンの場合
    if situation_input["menzen"] and situation_input["agari_situation"] == "ron":
        # 10符追加
        calc_dict["fu"] += 10

    # ツモの場合
    if situation_input["agari_situation"] == "tsumo":
        # 2符追加
        calc_dict["fu"] += 2

        # 平和ツモは20符固定
        if (is_pinfu):
            calc_dict["fu"] = 20

    if (is_pinfu):
        yaku_set.add("平和")
    
    # 喰い平和ロンは30符固定
    if (situation_input["agari_situation"] == "ron" and situation_input["formed_calls"] and calc_dict["fu"] == 20):
        calc_dict["fu"] = 30

    #1の位を切り上げる
    calc_dict["fu"] = helper.ceil(calc_dict["fu"], 1)
    return 

                                                                      
#     ▄▄▄▄                                                     ▄▄▄▄     
#   ██▀▀▀▀█                                                    ▀▀██     
#  ██         ▄████▄   ██▄████▄   ▄████▄    ██▄████   ▄█████▄    ██     
#  ██  ▄▄▄▄  ██▄▄▄▄██  ██▀   ██  ██▄▄▄▄██   ██▀       ▀ ▄▄▄██    ██     
#  ██  ▀▀██  ██▀▀▀▀▀▀  ██    ██  ██▀▀▀▀▀▀   ██       ▄██▀▀▀██    ██     
#   ██▄▄▄██  ▀██▄▄▄▄█  ██    ██  ▀██▄▄▄▄█   ██       ██▄▄▄███    ██▄▄▄  
#     ▀▀▀▀     ▀▀▀▀▀   ▀▀    ▀▀    ▀▀▀▀▀    ▀▀        ▀▀▀▀ ▀▀     ▀▀▀▀  

                                                        
def han_calc_general(situation_input, yaku_set) -> int:

    han = 0
    # 立直している場合
    # 副露牌がある場合は立直していないとみなす
    if not situation_input["formed_calls"]:
        if situation_input["riichi"] == 2:
            han += 2
            yaku_set.add("ダブル立直")
        elif situation_input["riichi"] == 1:
            han += 1
            yaku_set.add("立直")

    # 面前清自摸和の場合
    if situation_input["menzen"] and situation_input["agari_situation"] == "tsumo":
        han += 1
        yaku_set.add("門前清自摸和")
    
    # 槍槓の場合
    # 面前清自摸和と槍槓がどちらもTrueの場合、面前清自摸和を優先する
    if situation_input["chankan"] and situation_input["agari_situation"] == "ron":
        han += 1
        yaku_set.add("槍槓")

    # 嶺上開花の場合
    if situation_input["rinshan"] and situation_input["agari_situation"] == "tsumo":
        han += 1
        yaku_set.add("嶺上開花")

    # 海底摸月の場合
    # 海底摸月と嶺上開花がどちらもTrueの場合、嶺上開花を優先する
    if situation_input["last_tsumo"] and situation_input["agari_situation"] == "tsumo" and not situation_input["rinshan"]:
        han += 1
        yaku_set.add("海底摸月")

    # 河底撈魚の場合
    if situation_input["last_tsumo"] and situation_input["agari_situation"] == "ron":
        han += 1
        yaku_set.add("河底撈魚")

    # 一発の場合(嶺上開花と一発は共存しない)
    if situation_input["ippatsu"] and not situation_input["rinshan"]:
        han += 1
        yaku_set.add("一発")

    # ドラの計算
    dora = 0
    dora += sum(situation_input["hand_tiles"].count(dora_tile)  for dora_tile in situation_input["dora_tiles"])
    dora += sum(mentsu.count(dora_tile) for dora_tile in situation_input["dora_tiles"] for call_tiles in situation_input["call_tiles"] for mentsu in call_tiles["mentsu"])
    
    if dora > 0:
        han += dora
        yaku_set.add("ドラ" + str(dora))

    return han


#  ▄▄                                                          ▄▄▄▄               
#  ██                                                          ▀▀██               
#  ██▄████▄   ▄█████▄  ██▄████▄             ▄█████▄   ▄█████▄    ██       ▄█████▄ 
#  ██▀   ██   ▀ ▄▄▄██  ██▀   ██            ██▀    ▀   ▀ ▄▄▄██    ██      ██▀    ▀ 
#  ██    ██  ▄██▀▀▀██  ██    ██            ██        ▄██▀▀▀██    ██      ██       
#  ██    ██  ██▄▄▄███  ██    ██            ▀██▄▄▄▄█  ██▄▄▄███    ██▄▄▄   ▀██▄▄▄▄█ 
#  ▀▀    ▀▀   ▀▀▀▀ ▀▀  ▀▀    ▀▀              ▀▀▀▀▀    ▀▀▀▀ ▀▀     ▀▀▀▀     ▀▀▀▀▀  
#                               ▀▀▀▀▀▀▀▀▀▀                                        
def han_calc(formed_hand, situation_input, yaku_set, calc_dict) -> int:
    # 役満判定
    yakuman = ("清老頭","九蓮宝燈","大三元","小四喜","国士無双","緑一色","字一色","四暗刻","四槓子")
    double_yakuman = ("純正九蓮宝燈","大四喜","国士無双十三面待ち","四暗刻単騎待ち")
    
    yaku_set.add(check_chin_routou(situation_input["hand_tiles"], situation_input["formed_calls"]))
    yaku_set.add(check_chuuren_poutou(formed_hand["hand"][0], situation_input["menzen"], situation_input["agari_tile"]))
    yaku_set.add(check_daisangen(formed_hand, situation_input["formed_calls"]))
    yaku_set.add(check_daisuushi(formed_hand, situation_input["formed_calls"]))
    yaku_set.add(check_kokushi_musou(formed_hand["hand"][0], situation_input["menzen"], situation_input["agari_tile"]))
    yaku_set.add(check_ryu_iiso_tsu_iiso(situation_input["hand_tiles"], situation_input["formed_calls"]))
    yaku_set.add(check_su_anko(formed_hand, situation_input["agari_situation"]))
    yaku_set.add(check_su_kantsu(formed_hand, situation_input["formed_calls"]))

    # 役満の数、ダブル役満の数をカウント
    calc_dict["yakuman"] += len(yaku_set.intersection(yakuman))
    calc_dict["yakuman"] += 2 * len(yaku_set.intersection(double_yakuman))

    yaku_set.discard(None)

    # 役満があればリターン
    if (calc_dict["yakuman"] != 0):
        # 役満以外の役を削除
        yaku_set &= (set(yakuman) | set(double_yakuman))
        return

    # 状況で確定する役を取得
    calc_dict["han"] += han_calc_general(situation_input, yaku_set)

    # 役判定
    yaku_set.add("断么九" if check_tanyao(formed_hand, situation_input["formed_calls"]) else None)
    yaku_set.update(check_yaku_hai(situation_input["jikaze"], situation_input["bakaze"], formed_hand, situation_input["formed_calls"]))
    yaku_set.add("七対子" if check_chiitoitsu(formed_hand["hand"][0], situation_input["menzen"]) else None)
    yaku_set.add("一気通貫" if check_ikkitsuukan(formed_hand, situation_input["formed_calls"]) else None)
    yaku_set.add("三色同順" if check_sansyoku_dojun(formed_hand, situation_input["formed_calls"]) else None)
    yaku_set.add("三色同刻" if check_sansyoku_doko(formed_hand, situation_input["formed_calls"]) else None)
    yaku_set.add("対々和" if check_toitoi_ho(formed_hand, situation_input["formed_calls"]) else None)
    yaku_set.add(check_jun_chanta(formed_hand, situation_input["formed_calls"]))
    yaku_set.add(check_ryan_peekou(situation_input["menzen"], formed_hand))
    yaku_set.add(check_chin_iiso(situation_input["hand_tiles"], situation_input["call_tiles"]))

    yaku_set.discard(None)
    yaku_set.discard(False)

    # 翻数計算
    # yaku_setの要素ごとに翻数を追加
    for yaku in yaku_set:
        if yaku in const.yaku_han:
            calc_dict["han"] += const.yaku_han[yaku] - ((not situation_input["menzen"]) and yaku in const.kuisagari)

    return

                                                                                                    
#  ▄▄▄▄▄▄                 ██                                                       ▄▄▄▄               
#  ██▀▀▀▀█▄               ▀▀                 ██                                    ▀▀██               
#  ██    ██   ▄████▄    ████     ██▄████▄  ███████              ▄█████▄   ▄█████▄    ██       ▄█████▄ 
#  ██████▀   ██▀  ▀██     ██     ██▀   ██    ██                ██▀    ▀   ▀ ▄▄▄██    ██      ██▀    ▀ 
#  ██        ██    ██     ██     ██    ██    ██                ██        ▄██▀▀▀██    ██      ██       
#  ██        ▀██▄▄██▀  ▄▄▄██▄▄▄  ██    ██    ██▄▄▄             ▀██▄▄▄▄█  ██▄▄▄███    ██▄▄▄   ▀██▄▄▄▄█ 
#  ▀▀          ▀▀▀▀    ▀▀▀▀▀▀▀▀  ▀▀    ▀▀     ▀▀▀▀               ▀▀▀▀▀    ▀▀▀▀ ▀▀     ▀▀▀▀     ▀▀▀▀▀  
#                                                   ▀▀▀▀▀▀▀▀▀▀                                        
def point_calc(calc_dict):
    point_mangan = 2000
    if (calc_dict["yakuman"] != 0):     # 役満
        basic_point = int(point_mangan * 4.0 * calc_dict["yakuman"])

    elif (calc_dict["han"] >= 13):      # 数え役満
        basic_point = int(point_mangan * 4.0)
    
    elif (calc_dict["han"] >= 11):      # 三倍満
        basic_point = int(point_mangan * 3.0)

    elif (calc_dict["han"] >= 8):       # 倍満
        basic_point = int(point_mangan * 2.0)

    elif (calc_dict["han"] >= 6):       # 跳満
        basic_point = int(point_mangan * 1.5)

    elif (calc_dict["han"] >= 5):       # 満貫
        basic_point = int(point_mangan * 1.0)

    else:
        basic_point = (2 ** (calc_dict["han"] + 2)) * calc_dict["fu"]
        if (basic_point > 2000):        # 切り上げ満貫
            basic_point = point_mangan

    return basic_point
        
    
                                        
#  ▄▄▄  ▄▄▄               ██              
#  ███  ███               ▀▀              
#  ████████   ▄█████▄   ████     ██▄████▄ 
#  ██ ██ ██   ▀ ▄▄▄██     ██     ██▀   ██ 
#  ██ ▀▀ ██  ▄██▀▀▀██     ██     ██    ██ 
#  ██    ██  ██▄▄▄███  ▄▄▄██▄▄▄  ██    ██ 
#  ▀▀    ▀▀   ▀▀▀▀ ▀▀  ▀▀▀▀▀▀▀▀  ▀▀    ▀▀ 
                                        
def main_calc_process (situation_input):
    
    """
    麻雀の点数を計算する関数
    """
    # 役満数、翻、符を0で初期化する
    calc_dict = {"yakuman":0, "han":0, "fu":0}
    max_calc_dict = {"yakuman":0, "han":0, "fu":0}
    max_point = 0
    daten = ""

    # 役集合の宣言
    yaku_set = set()
    max_yaku_set = set()

    for formed_hand in situation_input["formed_hands"]:
        calc_dict = {"yakuman":0, "han":0, "fu":0}
        yaku_set.clear()
        if (not formed_hand):
            continue
        
        # 符計算
        fu_calc(formed_hand, situation_input, yaku_set, calc_dict)
        
        # 翻計算
        han_calc(formed_hand, situation_input, yaku_set, calc_dict)

        basic_point = point_calc(calc_dict)

        if (max_point, max_calc_dict["han"], max_calc_dict["fu"]) < (basic_point, calc_dict["han"], calc_dict["fu"]):
            max_point = basic_point
            max_yaku_set.clear()
            max_yaku_set = yaku_set.copy()
            max_calc_dict = calc_dict.copy()

    if (max_point > 8000):
        daten = str(calc_dict["yakuman"]).translate(num_to_kanji) + "倍役満"
    elif (max_point == 8000):
        if (max_calc_dict["yakuman"] == 0):
            daten = "数え役満"
        else:
            daten = "役満"
    elif (max_point == 6000):
        daten = "三倍満"
    elif (max_point == 4000):
        daten = "倍満"
    elif (max_point == 3000):
        daten = "跳満"
    elif (max_point == 2000):
        daten = "満貫"

    if (max_calc_dict["yakuman"] == 0 and max_calc_dict["han"] == 0):
        print("役がありませんでした")
        sys.exit()

    if (situation_input["agari_situation"] == "tsumo"): # ツモ
        payment_child = 0
        payment_host = 0
        if (situation_input["jikaze"] == "east"):   # 親
            payment_child = helper.ceil(max_point * 2, 2)   # 子の支払い
            payment_sum = payment_child * 3


        else:                                       # 子
            payment_child = helper.ceil(max_point, 2)       # 子の支払い
            payment_host = helper.ceil(max_point * 2, 2)    # 親の支払い
            payment_sum = payment_child * 2 + payment_host
            
        result = "合計: " + str(payment_sum) + " 子の支払い: " + str(payment_child)  + " 親の支払い: " + str(payment_host)


    elif (situation_input["agari_situation"] == "ron"): # ロン
        if (situation_input["jikaze"] == "east"):   # 親
            payment = helper.ceil(max_point * 6, 2)
            pass

        else:                                       # 子
            payment = helper.ceil(max_point * 4, 2)
        
        result = "合計: " + str(payment)

    else:
        print("エラー")

    a = [1,2,3]
    
    # 手牌表示の工夫
    hand_tiles = situation_input["hand_tiles"].copy()
    hand_tiles = [const.tiles[tile] for tile in hand_tiles]
    hand_tiles.sort()
    hand_tiles = [const.tiles_swap[tile] for tile in hand_tiles]
    hand_tiles.remove(situation_input["agari_tile"])
    call_tiles = [call_tile["mentsu"] for call_tile in situation_input["call_tiles"]]

    # 役表示の工夫
    final_yaku_list = []
    for yaku in const.yaku_sort:
        if yaku in yaku_set:
            final_yaku_list.append(yaku)
    
    for yaku in max_yaku_set:
        if "ドラ" in yaku:
            final_yaku_list.append(yaku)

    print(jaconv.alphabet2kata(situation_input["agari_situation"]))
    print(hand_tiles, call_tiles, situation_input["agari_tile"])
    print(result, daten)
    print(max_calc_dict)
    print(final_yaku_list)
    return
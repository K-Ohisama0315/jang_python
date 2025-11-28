from typing import TypedDict, List
import sys

from agari_pattern import agari_hands
from point_calculate import main_calc_process
from yaku_pattern import *

class FormedHands(TypedDict):
    hand: List[List[str]]           # 面子
    head: List[str]                 # 雀頭
    wait: str                       # 待ち方(ryanmen, penchan, kanchan, shanpon, tanki)

class CallTiles(TypedDict):
    calling: str                # 鳴き方(pon, chi, min_kan, ka_kan, an_kan)
    mentsu: List[str]               # 面子

class SituationInput(TypedDict):
    riichi: int				        # 立直(2:ダブル立直, 1:立直, 0:ダマ)
    menzen: bool                    # 面前
    agari_situation: str		    # ロンorツモ(ron, tsumo)
    last_tsumo: bool			    # ラスヅモ
    ippatsu: bool			        # 一発
    rinshan: bool			        # 嶺上開花
    chankan: bool			        # 槍槓
    jikaze: str	                    # 自風(east, south, west, north)
    bakaze: str	                    # 場風(east, south, west, north)
    agari_tile: str			        # アガリ牌
    dora_tiles: List[str]	        # ドラ牌
    red_dora_tiles: int             # 赤ドラの数
    hand_tiles: List[str]	        # 手牌
    formed_hands: FormedHands       # アガリ形
    call_tiles: List[CallTiles]		# 鳴き牌
    formed_calls: List[List[str]]   # 鳴き牌(暗槓抜き)

# デモ用（タンヤオのみ）
# riichi = 0
# agari_situation = "ron"
# last_tsumo = False
# ippatsu = False
# rinshan = False
# chankan = False
# jikaze = "east"
# bakaze = "east"
# agari_tile = "7m"
# dora_tiles = ["1s",]
# red_dora_tiles = 0
# hand_tiles = ["8s", "8s", "2s", "3s", "4s", "4p", "5p", "6p", "2m", "3m", "4m", "7m", "7m", "7m"]
# call_tiles = []

# デモ用（リーヅモタンヤオドラ２）
# riichi = 1
# agari_situation = "tsumo"
# last_tsumo = False
# ippatsu = False
# rinshan = False
# chankan = False
# jikaze = "east"
# bakaze = "east"
# agari_tile = "7m"
# dora_tiles = ["8s", "1m"]
# red_dora_tiles = 0
# hand_tiles = ["8s", "8s", "2s", "3s", "4s", "4p", "5p", "6p", "2m", "3m", "4m", "7m", "7m", "7m"]
# call_tiles = []

# デモ用（国士無双）
riichi = 0
agari_situation = "ron"
last_tsumo = False
ippatsu = False
rinshan = False
chankan = False
jikaze = "east"
bakaze = "east"
agari_tile = "red"
dora_tiles = ["1s",]
red_dora_tiles = 0
hand_tiles = ["1s", "9s", "1m", "9m", "1p", "9p", "east", "west", "south", "north", "white", "green", "red", "1m"]
call_tiles = []

# 6倍役満
# riichi = 0
# agari_situation = "tsumo"
# last_tsumo = False
# ippatsu = False
# rinshan = False
# chankan = False
# jikaze = "east"
# bakaze = "east"
# agari_tile = "white"
# dora_tiles = ["1s",]
# red_dora_tiles = 0
# hand_tiles = ["white","white"]  # 字一色、四暗刻単騎、大四喜、四槓子
# call_tiles = [{"calling":"an_kan", "mentsu": [["east", "east", "east", "east"],["south", "south", "south", "south"],["west", "west", "west", "west"],["north", "north", "north", "north"]]},]

situation_input:SituationInput = {
    "riichi": riichi,
    "menzen": not call_tiles,
    "agari_situation": agari_situation, 
    "last_tsumo": last_tsumo, 
    "ippatsu": ippatsu, 
    "rinshan": rinshan, 
    "chankan": chankan, 
    "jikaze": jikaze, 
    "bakaze": bakaze,
    "agari_tile": agari_tile,
    "dora_tiles": dora_tiles, 
    "red_dora_tiles":red_dora_tiles,
    "hand_tiles": hand_tiles, 
    "formed_hands": [],
    "call_tiles": call_tiles,
    "formed_calls": []

}

if (not situation_input["agari_tile"] in situation_input["hand_tiles"]):
    print("手牌にアガリ牌が含まれていません")
    sys.exit()

agari_hands.main_agari_process(situation_input)
if not situation_input["formed_hands"]:
    print("アガリ形が存在しませんでした")
    sys.exit()

situation_input["menzen"] = not situation_input["formed_calls"]

main_calc_process(situation_input)

# hand_tiles = ["","","","","","","","","","","","","",""]
# hand_tiles = ["2m","3m","4m","8m","8m","5s","6s","6s","7s","7s","8s","2p","3p","4p"] # 断幺
# hand_tiles = ["5m", "7s", "white", "2p", "6m", "4p", "white", "7s", "3p", "4m", "white", "east", "east", "east"] # 白、東
# hand_tiles = ["1m", "1m", "1m", "1m", "2m", "2m", "2m", "2m", "3m", "3m", "3m", "3m", "4m", "4m"] # 清一色、二盃口
# hand_tiles = ["7s","9s","5s","1s","8s","1s","9s","1s","6s","4s","9s","3s","6s","2s"] # 九蓮宝燈
# hand_tiles = ["1s","1s","1s","2s","3s","4s","5s","6s","7s","7s","8s","9s","9s","9s"] # 九蓮宝燈
# hand_tiles = ["2p","2p","4s","white","6p","west","6p","1m","4s","3s","west","3s","1m","white"] # 七対子
# hand_tiles = ["south","9p","1s","9s","1p","west","west","east","north","red","1m","white","9m","green"] # 国士無双
# hand_tiles = ["3p","7s","4m","4p","4m","4p","9s","3p","7s","8s","5p","5p","8s","9s"] # 七対子もしくは二盃口
# hand_tiles = ["6s","3s","8s","2s","6s","3s","2s","green","2s","green","6s","green","8s","8s"] #緑一色
# hand_tiles = ["white","east","east","north","red","west","white","west","white","east","north","north","red","red"] # 字一色
# hand_tiles = ["1m","1p","1s","east","1p","1m","1s","east","1m","1p","1s","west","east","west"] #混老頭、三色同刻、東
# hand_tiles = ["1m","1p","1s","9p","1p","1m","1s","9m","1m","1p","1s","9p","9m","9p"] #清老頭
# hand_tiles = ["2p","4p","3p","3p","1p","4m","green","4m","3p","3p","5p","green","4m","green"] # 3pで辺張、両面、単騎
# hand_tiles = ["1p","2p","3p","3p","3p","3p","4p","4p","4p","5p","5p","5p","6p","6p"]
# hand_tiles = ["east","east","south","south","west","west","north","north","white","white","green","green","red","red"]  # 大七星(七対子字一色)
# hand_tiles = ["east","east","east","south","south","south","west","west","west","north","north","north","red","red"]  # 大四喜
# hand_tiles = ["white","white","white","green","green","green","red","red","red","9p","9p","4s","5s","6s"]


# hand_tiles = ["1m","1m"] #混全帯么九、東、發
# call_tiles = [{"calling":"an_kan", "mentsu": [["east", "east", "east", "east"],]},{"calling":"chi", "mentsu":[["1p","2p","3p"],]}, {"calling":"pon", "mentsu":[["1s","1s","1s"],["green", "green", "green"]]}]

# hand_tiles = ["east","east","east","north","north","north","red","red","red","white","white"] #字一色
# call_tiles = [{"calling":"pon", "mentsu": [[ "green", "green", "green"],]},]

# hand_tiles = ["white","white"]  # 字一色、四暗刻単騎、大四喜、四槓子
# call_tiles = [{"calling":"an_kan", "mentsu": [["east", "east", "east", "east"],["south", "south", "south", "south"],["west", "west", "west", "west"],["north", "north", "north", "north"]]},]


# print("清一色のやつ", check_chin_iiso(situation_input))
# print("混老頭のやつ", check_hon_routou(situation_input))
# print("清老頭のやつ", check_chin_routou(situation_input))

# yaku_set = set()
# for formed_hand in situation_input["formed_hands"]:
#     # print("九蓮宝燈チェック:", check_chuuren(formed_hand["hand"][0], situation_input["menzen"], situation_input["agari_tile"]))
#     # print("国士無双チェック:", check_kokushi_musou(formed_hand["hand"][0], situation_input["menzen"], situation_input["agari_tile"]))
#     # print("緑一色字一色チェック:", check_ryu_iiso_tsu_iiso(situation_input["hand_tiles"], situation_input["formed_calls"]))
#     # print("清老頭混老頭チェック:", check_chin_routou(situation_input["hand_tiles"], situation_input["formed_calls"]))
   
#     yaku_set.add(check_chin_routou(situation_input["hand_tiles"], situation_input["formed_calls"]))
#     yaku_set.add(check_chuuren_poutou(formed_hand["hand"][0], situation_input["menzen"], situation_input["agari_tile"]))
#     yaku_set.add(check_daisangen(formed_hand, situation_input["formed_calls"]))
#     yaku_set.add(check_daisuushi(formed_hand, situation_input["formed_calls"]))
#     yaku_set.add(check_kokushi_musou(formed_hand["hand"][0], situation_input["menzen"], situation_input["agari_tile"]))
#     yaku_set.add(check_ryu_iiso_tsu_iiso(situation_input["hand_tiles"], situation_input["formed_calls"]))
#     yaku_set.add(check_su_anko(formed_hand))
#     yaku_set.add(check_su_kantsu(formed_hand, situation_input["formed_calls"]))


# for formed_hand in situation_input["formed_hands"]:
#     # print("七対子チェック:", check_chiitoitsu(formed_hand["hand"][0], situation_input["menzen"]))

#     yaku_set.add("断幺" if check_tanyao(formed_hand, situation_input["formed_calls"]) else None)
#     a = (check_yaku_hai(situation_input["jikaze"], situation_input["bakaze"], formed_hand, situation_input["formed_calls"]))
#     yaku_set.add("七対子" if check_chiitoitsu(formed_hand["hand"][0], situation_input["menzen"]) else None)
#     yaku_set.add("一気通貫" if check_ikkitsuukan(formed_hand, situation_input["formed_calls"]) else None)
#     yaku_set.add("三色同順" if check_sansyoku_dojun(formed_hand, situation_input["formed_calls"]) else None)
#     yaku_set.add("三色同刻" if check_sansyoku_doko(formed_hand, situation_input["formed_calls"]) else None)
#     yaku_set.add("対々和" if check_toitoi_ho(formed_hand, situation_input["formed_calls"]) else None)
#     yaku_set.add(check_jun_chanta(formed_hand, situation_input["formed_calls"]))
#     yaku_set.add(check_ryan_peekou(situation_input["menzen"], formed_hand))
#     yaku_set.add(check_chin_iiso(situation_input["hand_tiles"], situation_input["formed_calls"]))

a = 0
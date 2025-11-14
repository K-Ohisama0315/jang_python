from typing import TypedDict, List

from agari_pattern import agari_hands
from yaku_pattern import *

class FormedHands(TypedDict):
    hand: List[List[str]]           #面子
    head: List[str]                 #雀頭

class SituationInput(TypedDict):
    riichi: int				        #立直(2:ダブル立直, 1:立直, 0:ダマ)
    menzen: bool                    #面前
    agari_situation: str		    #ロンorツモ(ron, tsumo)
    last_tsumo: bool			    #ラスヅモ
    ippatsu: bool			        #一発
    rinshan: bool			        #嶺上開花
    chankan: bool			        #槍槓
    jikaze: str	                    #自風(east, south, west, north)
    bakaze: str	                    #場風(east, south, west, north)
    agari_tile: str			        #アガリ牌
    display_dora_tiles: List[str]	#ドラ表示牌
    hand_tiles: List[str]	        #手牌
    formed_hands: FormedHands       #アガリ形
    call_tiles: List[List[str]]		#鳴き牌

# 暫定値(立直、一発、二盃口、)
riichi = 1                              #立直あり
agari_situation = "ron"                 #ロンアガリ
last_tsumo = False                      #ラスヅモではない
ippatsu = True			                #一発
rinshan = False			                #嶺上開花
chankan = False			                #槍槓
jikaze = "south"	                    #自風(east, south, west, north)
bakaze = "east"	                        #場風(east, south, west, north)
agari_tile = "white"			        #アガリ牌
display_dora_tiles = ["3m", "white"]	#ドラ表示牌
hand_tiles = ["1m","1p","1s","9p","1p","1m","1s","9m","1m","1p","1s","9p","9m","9p"] #清老頭
call_tiles = []                         #鳴き牌

situation_input:SituationInput = {
    "riichi": riichi,
    "menzen": not call_tiles, 
    "agari_situation": agari_situation, 
    "last_tsumo": last_tsumo, 
    "ippatsu": ippatsu, 
    "rinshan": rinshan, 
    "chankan": rinshan, 
    "jikaze": jikaze, 
    "bakaze": bakaze,
    "agari_tile": agari_tile,
    "display_dora_tiles": display_dora_tiles, 
    "hand_tiles": hand_tiles, 
    "formed_hands": [],
    "call_tiles": call_tiles
}

agari_hands.main_agari_process(situation_input)


# hand_tiles = ["5m", "7s", "white", "2p", "6m", "4p", "white", "7s", "3p", "4m", "white", "east", "east", "east"] # 白、東
# hand_tiles = ["1m", "1m", "1m", "1m", "2m", "2m", "2m", "2m", "3m", "3m", "3m", "3m", "4m", "4m"] # 清一色、二盃口
# hand_tiles = ["7s","9s","5s","1s","8s","1s","9s","1s","6s","4s","9s","3s","6s","2s"] # 九蓮宝燈
# hand_tiles = ["2p","2p","4s","white","6p","west","6p","1m","4s","3s","west","3s","1m","white"] # 七対子
# hand_tiles = ["south","9p","1s","9s","1p","west","west","east","north","red","1m","white","9m","green"] # 国士無双
# hand_tiles = ["3p","7s","4m","4p","4m","4p","9s","3p","7s","8s","5p","5p","8s","9s"] # 七対子もしくは二盃口
# hand_tiles = ["6s","3s","8s","2s","6s","3s","2s","green","2s","green","6s","green","8s","8s"] #緑一色
# hand_tiles = ["white","east","east","north","red","west","white","west","white","east","north","north","red","red"] # 字一色
# hand_tiles = ["1m","1p","1s","east","1p","1m","1s","east","1m","1p","1s","west","east","west"] #混老頭、三色同刻
# hand_tiles = ["1m","1p","1s","9p","1p","1m","1s","9m","1m","1p","1s","9p","9m","9p"] #清老頭
# hand_tiles = ["","","","","","","","","","","","","",""]


# print("九蓮宝燈のやつ",check_chuuren(situation_input))
# print("七対子のやつ", check_chiitoitsu(situation_input))
# print("国士無双のやつ", check_kokushi_musou(situation_input))
# print("清一色のやつ", check_chin_iiso(situation_input))
# print("緑一色のやつ", check_ryu_iiso(situation_input))
# print("字一色のやつ", check_tsu_iiso(situation_input))
print("混老頭のやつ", check_hon_routou(situation_input))
print("清老頭のやつ", check_chin_routou(situation_input))
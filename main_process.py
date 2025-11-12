from typing import TypedDict, List
import pprint

from agari_pattern import agari_hands

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

# 暫定値
riichi = 1                              #立直あり
agari_situation = "ron"                 #ロンアガリ
last_tsumo = False                      #ラスヅモではない
ippatsu = True			                #一発
rinshan = False			                #嶺上開花
chankan = False			                #槍槓
jikaze = "south"	                    #自風(east, south, west, north)
bakaze = "east"	                        #場風(east, south, west, north)
agari_tile = "4m"			            #アガリ牌
display_dora_tiles = ["3m", "white"]	#ドラ表示牌
hand_tiles = ["1m", "1m", "1m", "1m", "2m", "2m", "2m", "2m", "3m", "3m", "3m", "3m", "4m", "4m"]    #手牌
call_tiles = []

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
    "formed_hands": agari_hands.main_agari_process(hand_tiles),
    "call_tiles": call_tiles
}

#hand_tiles = {"hand":["5m", "7s", "white", "2p", "6m", "4p", "white", "7s", "3p", "4m", "white", "east", "east", "east"], "call":[[],]}

#hand_tiles = {"hand":["1m", "1m", "1m", "1m", "2m", "2m", "2m", "2m", "3m", "3m", "3m", "3m", "4m", "4m"], "call":[[],]}


pprint.pprint(situation_input)


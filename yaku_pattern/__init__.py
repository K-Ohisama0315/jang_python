# 一翻
from .yaku_1han.tanyao import check_tanyao
from .yaku_1han.haku import check_haku

# 二翻
from .yaku_2han.chiitoitsu import check_chiitoitsu
from .yaku_2han.hon_routou import check_hon_routou

# 六翻
from .yaku_6han.chin_iiso import check_chin_iiso

# 役満
from .yakuman.kokushi_musou import check_kokushi_musou
from .yakuman.chuuren_poutou import check_chuuren
from .yakuman.ryu_iiso import check_ryu_iiso
from .yakuman.tsu_iiso import check_tsu_iiso
from .yakuman.chin_routou import check_chin_routou

# initファイルで外部に公開する関数を定義
__all__ = [
    "check_tanyao",
    "check_haku",

    "check_chiitoitsu",
    "check_hon_routou",

    "check_chin_iiso",

    "check_kokushi_musou",
    "check_chuuren",
    "check_ryu_iiso",
    "check_tsu_iiso",
    "check_chin_routou"

]
import math

# 点数を百の位で切り上げるヘルパー関数
def ceil(points, power):
    return math.ceil(points / (10 ** power)) * (10 ** power)
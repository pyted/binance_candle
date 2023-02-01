from binance_candle.exception._base import AbstractEXP

# 参数异常
class ParamException(AbstractEXP):
    def __init__(self, msg):
        self.error_msg = msg

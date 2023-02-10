from binance_candle.server.rule import CandleRule
from binance_candle.server.server import CandleServer


class CandleServerSPOT(CandleServer):
    def __init__(self, rule):
        instType = 'SPOT'
        super(CandleServerSPOT, self).__init__(instType=instType, rule=rule)


class CandleServerUM(CandleServer):
    def __init__(self, rule):
        instType = 'UM'
        super(CandleServerUM, self).__init__(instType=instType, rule=rule)


class CandleServerCM(CandleServer):
    def __init__(self, rule):
        instType = 'Cm'
        super(CandleServerCM, self).__init__(instType=instType, rule=rule)

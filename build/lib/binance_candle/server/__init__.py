from binance_candle.server.rule import CandleRule
from binance_candle.server.server import CandleServer


class SpotCandleServer(CandleServer):
    def __init__(self, rule):
        instType = 'SPOT'
        super(SpotCandleServer, self).__init__(instType=instType, rule=rule)


class UmCandleServer(CandleServer):
    def __init__(self, rule):
        instType = 'UM'
        super(UmCandleServer, self).__init__(instType=instType, rule=rule)


class CmCandleServer(CandleServer):
    def __init__(self, rule):
        instType = 'Cm'
        super(CmCandleServer, self).__init__(instType=instType, rule=rule)

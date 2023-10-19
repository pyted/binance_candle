from binance_candle.server.rule import CandleRule
from binance_candle.server.server import CandleServer


class CandleServerSPOT(CandleServer):
    def __init__(self, rule, proxies={}, proxy_host: str = None):
        instType = 'SPOT'
        super(CandleServerSPOT, self).__init__(instType=instType, rule=rule, proxies=proxies, proxy_host=proxy_host)


class CandleServerUM(CandleServer):
    def __init__(self, rule, proxies={}, proxy_host: str = None):
        instType = 'UM'
        super(CandleServerUM, self).__init__(instType=instType, rule=rule, proxies=proxies, proxy_host=proxy_host)


class CandleServerCM(CandleServer):
    def __init__(self, rule, proxies={}, proxy_host: str = None):
        instType = 'Cm'
        super(CandleServerCM, self).__init__(instType=instType, rule=rule, proxies=proxies, proxy_host=proxy_host)

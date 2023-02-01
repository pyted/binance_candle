from binance_candle.market.history_candle import HistoryCandle  # 历史K线
from binance_candle.market.exchange_info import ExchangeInfo  # 交易对信息
from binance_candle.market.ticker import Ticker  # 实时价格

__all__ = ['Market', 'SpotMarket', 'UmMarket', 'CmMarket']


class Market(HistoryCandle, Ticker, ExchangeInfo):
    pass


class SpotMarket(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York'):
        instType = 'SPOT'
        super(SpotMarket, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone)


class UmMarket(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York'):
        instType = 'UM'
        super(UmMarket, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone)


class CmMarket(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York'):
        instType = 'CM'
        super(CmMarket, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone)

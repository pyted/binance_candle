from binance_candle.market.history_candle import HistoryCandle  # 历史K线
from binance_candle.market.exchange_info import ExchangeInfo  # 交易对信息
from binance_candle.market.ticker import Ticker  # 实时价格

__all__ = ['Market', 'MarketSPOT', 'MarketUM', 'MarketCM']


class Market(HistoryCandle, Ticker, ExchangeInfo):
    pass


class MarketSPOT(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York'):
        instType = 'SPOT'
        super(MarketSPOT, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone)


class MarketUM(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York'):
        instType = 'UM'
        super(MarketUM, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone)


class MarketCM(Market):
    def __init__(self, key: str = '', secret: str = '', timezone: str = 'America/New_York'):
        instType = 'CM'
        super(MarketCM, self).__init__(instType=instType, key=key, secret=secret, timezone=timezone)

from binance_candle import Market
from pprint import pprint

if __name__ == '__main__':
    # 币币交易：SPOT；U本位合约：UM；币本位合约：CM
    instType = 'SPOT'
    # 实例化行情Market
    market = Market(instType)
    # 全部产品的最优挂单
    pprint(market.get_bookTickersMap())  # 字典类型
    pprint(market.get_bookTickers())  # 列表类型
    # 单个产品的最优挂单（BTTUSDT）
    pprint(market.get_bookTicker('BTCUSDT'))


from binance_candle import Market
from pprint import pprint

if __name__ == '__main__':
    proxy_host = None # http://xxx.xx.xx.xx
    # 币币交易：SPOT；U本位合约：UM；币本位合约：CM
    instType = 'SPOT'
    # 实例化行情Market
    market = Market(instType,proxy_host=proxy_host)
    # 全部产品的最新成交价格
    pprint(market.get_tickerPricesMap())  # 字典类型
    pprint(market.get_tickerPrices())  # 列表类型
    # 单个产品的最新成交价格（BTTUSDT）
    pprint(market.get_tickerPrice('BTCUSDT'))

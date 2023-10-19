from binance_candle import Market
from pprint import pprint

if __name__ == '__main__':
    proxy_host = None # http://xxx.xx.xx.xx
    # 币币交易：SPOT；U本位合约：UM；币本位合约：CM
    instType = 'SPOT'
    # 实例化行情Market
    market = Market(instType,proxy_host=proxy_host)
    # 可以交易的产品列表
    pprint(market.get_symbols_trading_on())
    # 不可以交易的产品列表
    pprint(market.get_symbols_trading_off())

from binance_candle import Market
from pprint import pprint

if __name__ == '__main__':
    # 币币交易：SPOT；U本位合约：UM；币本位合约：CM
    instType = 'SPOT'
    # 实例化行情Market
    market = Market(instType)
    # 产品类型的全部交易规范
    exchangeInfos = market.get_exchangeInfos()
    pprint(exchangeInfos)
    # BTCUSDT的交易规范
    BTCUSDT_enchangeInfo = market.get_exchangeInfo('BTCUSDT')
    pprint(BTCUSDT_enchangeInfo)

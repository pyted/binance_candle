from binance_candle import Market
from pprint import pprint

if __name__ == '__main__':
    # 币币交易：SPOT；U本位合约：UM；币本位合约：CM
    instType = 'UM'
    # 实例化行情Market
    market = Market(instType, timezone='America/New_York')
    # 获取历史K线接口中最新数据的毫秒时间戳
    result = market.get_history_candle_latest_ts(bar='1m')
    pprint(result)
    # 按照起始时间获取历史K线
    result = market.get_history_candle(
        symbol='BTCUSDT',
        start='2023-01-01 00:00:00',
        end='2023-01-01 10:00:00',
        bar='1m',
    )
    pprint(result)
    # 按照日期下载历史K线
    result = market.get_history_candle_by_date(
        symbol='BTCUSDT',
        date='2023-01-01',
        bar='1m'
    )
    pprint(result)
    # 将candle更新到最新，长度为length
    result = market.update_history_candle(
        symbol='BTCUSDT',
        candle=result['data'],  # None 表示重新获取
        length=1440,
        bar='1m',
    )
    pprint(result)

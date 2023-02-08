from binance_candle import CandleServer, CandleRule
import time
from pprint import pprint
from binance_candle.utils import candle_to_df

if __name__ == '__main__':
    # 币币交易：SPOT；U本位合约：UM；币本位合约：CM
    instType = 'UM'
    # 永续合约，默认规则
    candleServer = CandleServer(instType, CandleRule)
    # 启动K线维护服务
    candleServer.run_candle_map()
    # 被异步维护的candle_map字典
    pprint(candleServer.candle_map)
    # 打印实时更新的candle
    for i in range(120):
        # 以安全的方式从candle_map中获取历史线
        candle = candleServer.get_candle_security('BTCUSDT')
        pprint(candle)  # 类型：np.ndarray
        pprint(candle_to_df(candle))  # 类型：pd.DataFrame
        time.sleep(1)
    # 关闭服务
    candleServer.close_run_candle_map()

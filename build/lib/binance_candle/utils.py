from typing import Union
from copy import deepcopy
import numpy as np
import pandas as pd
from candlelite.crypto.binace_lite import BINANCE_TIMEZONE
from candlelite.calculate.transform import to_candle as _to_candle
from paux import date as _date


# 将Binance的历史K线数据从array转换成DataFrame类型
def candle_to_df(
        candle: np.ndarray,
        convert_ts: bool = True,
        timezone: Union[str, None] = BINANCE_TIMEZONE,
) -> pd.DataFrame:
    '''
    :param candle: array类型的历史K线数据
    :param convert_ts: 是否将时间戳转化为日期字符串
    :param timezone: 时区
        默认使用candlelite中Binance的时区
        None 使用本机默认时区
    '''
    df = pd.DataFrame(candle)
    df.columns = [
        'openTs',  # 开盘时间 Open time
        'open',  # 开盘价 Open
        'high',  # 最高价 High
        'low',  # 最低价 Low
        'close',  # 收盘价(当前K线未结束的即为最新价) Close
        'volume',  # 成交量 Volume
        'closeTs',  # 收盘时间 Close time
        'turnover',  # 成交额 Quote asset volume
        'tradeNum',  # 成交笔数 Number of trades
        'buyVolume',  # 主动买入成交量 Taker buy base asset volume
        'buyTurnover',  # 主动买入成交额 Taker buy quote asset volume
        'ignore'  # 请忽略该参数 Ignore
    ]
    df = df.drop(columns=['ignore'])
    # 是否转换时间戳为日期字符串
    if convert_ts:
        # 美国时间
        if timezone == 'America/New_York':
            fmt = '%m/%d/%Y %H:%M:%S'
        # 中国时间
        else:
            fmt = '%Y-%m-%d %H:%M:%S'
        df['openTs'] = df['openTs'].apply(
            lambda openTs: _date.to_fmt(date=openTs, timezone=timezone, fmt=fmt)
        )
        df['closeTs'] = df['closeTs'].apply(
            lambda closeTs: _date.to_fmt(date=closeTs, timezone=timezone, fmt=fmt)
        )
    return df


# 将Binance的历史K线数据从DataFrame转换成array类型
def df_to_candle(
        df: pd.DataFrame,
        timezone: Union[str,None]= BINANCE_TIMEZONE
):
    '''
    :param df: DataFrame类型的历史K线数据
    :param timezone: 时区
        默认使用candlelite中Binance的时区
        None 使用本机默认时区
    '''
    df = deepcopy(df)
    df['openTs'] = df['openTs'].apply(
        lambda openTs: _date.to_ts(date=openTs, timezone=timezone)
    )
    df['closeTs'] = df['closeTs'].apply(
        lambda closeTs: _date.to_ts(date=closeTs, timezone=timezone)
    )
    candle = _to_candle(df)
    return candle

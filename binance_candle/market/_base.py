from typing import Literal
import pbinance
from binance_candle import exception


# 市场信息基类
class MarketBase(pbinance.Binance):

    def __init__(
            self,
            instType: Literal['SPOT', 'UM', 'CM'],
            key: str = '',
            secret: str = '',
            timezone='America/New_York'
    ):
        '''
        主要为了处理inst
            instType = 'SPOT'   self.inst -> self.spot
            instType = 'UM'     self.inst -> self.um
            instType = 'CM'     self.inst -> self.cm

        :param instType: 产品类型
            SPOT:   现货
            UM:     U本位合约
            CM:     币本位合约
        :param key: API KEY 可以不填写
        :param secret: API SECRET 可以不填写
        :param timezone: 时区
            America/New_York:   美国时间
            Asia/Shanghai:      中国时间
        '''
        # 父类
        super(MarketBase, self).__init__(key=key, secret=secret)
        # 时区与产品类别
        self.timezone = timezone
        self.instType = instType.upper()
        # inst
        if self.instType == 'SPOT':  # 现货交易
            self.inst = self.spot
        elif self.instType == 'UM':  # U本位
            self.inst = self.um
        elif self.instType == 'CM':  # 币本位
            self.inst = self.cm
        else:
            msg = '[instType error] your input instType={instType} instType must in ["SPOT","UM","CM","EO"]'.format(
                instType=str(instType)
            )
            raise exception.ParamException(msg)

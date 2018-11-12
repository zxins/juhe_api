# -*- coding:utf-8 -*-
import json
import requests
from exc.exception import BizError


class JuheNews(object):
    """
    类型,,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
    """

    def __init__(self):

        self.key = 'dd406a5a02288cbe8b0a8b8b3c05f852'
        self.host = 'http://v.juhe.cn/toutiao/index'

    def get_news(self, news_type=None):

        try:

            params = {
                'type': news_type,
                'key': self.key,
            }

            r = requests.get(self.host, params=params)
            r.encoding = r.apparent_encoding
            js_content = json.loads(r.content)

            error_code = str(js_content.get('error_code'))
            if not error_code or str(error_code) != '0':
                raise BizError('juhe error: {0}'.format(js_content.get('reason')))

            result = js_content.get('result')
            data = result.get('data')
            return data

        except Exception as e:
            import traceback
            traceback.print_exc()
            raise e

    @property
    def top(self):

        return self.get_news('top')

    @property
    def shehui(self):

        return self.get_news('shehui')

    @property
    def guonei(self):

        return self.get_news('guonei')

    @property
    def guoji(self):

        return self.get_news('guoji')

    @property
    def yule(self):

        return self.get_news('yule')

    @property
    def tiyu(self):

        return self.get_news('tiyu')

    @property
    def junshi(self):

        return self.get_news('junshi')

    @property
    def keji(self):

        return self.get_news('keji')

    @property
    def caijing(self):

        return self.get_news('caijing')

    @property
    def shishang(self):

        return self.get_news('shishang')

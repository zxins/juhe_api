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

    def __get_news(self, news_type=None):

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
        """ 头条, 默认 """
        return self.__get_news('top')

    @property
    def shehui(self):
        """ 社会 """
        return self.__get_news('shehui')

    @property
    def guonei(self):
        """ 国内 """
        return self.__get_news('guonei')

    @property
    def guoji(self):
        """ 国际 """
        return self.__get_news('guoji')

    @property
    def yule(self):
        """ 娱乐 """
        return self.__get_news('yule')

    @property
    def tiyu(self):
        """ 体育 """
        return self.__get_news('tiyu')

    @property
    def junshi(self):
        """ 军事 """
        return self.__get_news('junshi')

    @property
    def keji(self):
        """ 科技 """
        return self.__get_news('keji')

    @property
    def caijing(self):
        """ 财经 """
        return self.__get_news('caijing')

    @property
    def shishang(self):
        """ 时尚 """
        return self.__get_news('shishang')

    @property
    def all(self):
        news = list()
        news.extend(self.top)
        news.extend(self.guonei)
        news.extend(self.guoji)
        news.extend(self.yule)
        news.extend(self.tiyu)
        news.extend(self.junshi)
        news.extend(self.keji)
        news.extend(self.caijing)
        news.extend(self.shishang)
        return news


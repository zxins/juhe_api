# -*- coding: utf-8 -*-

from xpinyin import Pinyin

# TODO: 这个写法太丑了
CATEGORIES = {
    'top': [
        'TOP',
        '头条',
        'DEFAULT',
        'TOUTIAO'
    ],
    'shehui': [
        'SHEHUI',
        '社会'
    ],
    'guonei': [
        'GUONEI',
        '国内'
    ],
    'guoji': [
        'GUOJI',
        '国际'
    ],
    'yule': [
        'YULE',
        '娱乐'
    ],
    'tiyu': [
        'TIYU',
        '体育'
    ],
    'junshi': [
        'JUNSHI',
        '军事'
    ],
    'keji': [
        'KEJI',
        '科技'
    ],
    'caijing': [
        'CAIJING',
        '财经'
    ],
    'shishang': [
        'SHISHANG',
        '时尚'
    ],
}


def pinyin(text):
    p = Pinyin()
    return p.get_pinyin(text, '')


def get_category(text):
    if not text:
        return 'top'
    if type(text) == unicode:
        text = text.encode('utf-8')

    category = 'top'  # 默认值
    py = pinyin(text).upper()
    for key, values in CATEGORIES.iteritems():
        for val in values:
            if py in val:
                category = key
                break
    return category

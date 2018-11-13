# -*- coding: utf-8 -*-

def vo_format_news(news):
    vo = {
        'title': news.title,
        'author_name': news.author_name,
        'date': news.date,
        'url': news.url,
        'pictures': news.pictures,
        'category': news.category,
    }
    return vo

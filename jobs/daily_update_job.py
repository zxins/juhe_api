# -*- coding:utf-8 -*-

from entity.news import News
from facade.juhe.news import JuheNews
from repository.mysql.news import NewsRepository


def update_news():
    try:
        jn = JuheNews()

        news = list()
        for row in jn.all:
            i = 0
            pictures = dict()
            for k, v in row.items():
                if 'thumbnail' in k:
                    i += 1
                    key = 'img{0}'.format(str(i))
                    pictures[key] = v

            param = {
                'no': row.get('uniquekey'),
                'title': row.get('title'),
                'author_name': row.get('author_name'),
                'url': row.get('url'),
                'date': row.get('date'),
                'category': row.get('category'),
                'pictures': pictures,
            }
            news.append(News(**param))

        nr = NewsRepository()
        nr.batch_save(news)

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e


if __name__ == '__main__':
    update_news()

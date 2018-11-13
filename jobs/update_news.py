# -*- coding:utf-8 -*-
from entity.news import News
from facade.juhe.news import JuheNews
from repository.mysql.news import NewsRepository


def update_news():
    try:
        jn = JuheNews()

        news = list()
        for row in jn.all:
            pictures = get_pictures(row)
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


def get_pictures(data):
    i = 0
    pictures = dict()
    for k, v in data.items():
        if 'thumbnail' in k:
            i += 1
            key = 'img{0}'.format(str(i))
            pictures[key] = v
    return pictures


def start_cron_job():
    """ 定时任务入口 """

    import time
    import schedule

    schedule.every().day.at('08:00').do(update_news)
    schedule.every().day.at('12:00').do(update_news)

    while True:
        schedule.run_pending()
        time.sleep(2)


if __name__ == '__main__':
    start_cron_job()

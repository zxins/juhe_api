# -*- coding: utf-8 -*-

import sys

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from config import MYSQL_HOST, MYSQL_PASS, MYSQL_USER, MYSQL_DB

reload(sys)
sys.setdefaultencoding('utf8')

Base = automap_base()

# 数据库连接配置
MYSQL_CONN = 'mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8'.format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_DB)

database = create_engine(MYSQL_CONN, pool_recycle=30, pool_size=100)

# 默认自动flush（一旦flush就能在query中拿到数据），但是不自动提交（不提交就不会真的写到数据库中去），
# 由程序自己控制，这样有利于事务的控制
DBSession = sessionmaker(bind=database, autoflush=True, autocommit=False, expire_on_commit=True)


def get_session():
    ''' 每次返回一个session的实例就实际上从连接池里面拿走一个conn，从conn可以拿出一个transaction（事务）来用 '''
    return DBSession()


class NewsModel(Base):
    """ 新闻Model """

    __tablename__ = 'news'


Base.prepare(database, reflect=True)

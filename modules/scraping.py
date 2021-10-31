from bs4 import BeautifulSoup
from urllib.request import urlopen
from config import databases
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, VARCHAR, TEXT
from sqlalchemy.orm import sessionmaker
from modules.coin_bot import send_message
import time

engine = create_engine(databases.DB_URI)
DB = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()


class binance_notice(DB):
    __tablename__ = 'binance_notice'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(300))
    text = Column(VARCHAR(300))

    @staticmethod
    def add(url, text):
        stu = binance_notice(url=url, text=text)
        session.add(stu)
        session.commit()

    @staticmethod
    def truncate():
        sql = """truncate table binance_notice"""
        session.execute(sql)
        session.commit()


class binance_notice_temp(DB):
    __tablename__ = 'binance_notice_temp'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(300))
    text = Column(VARCHAR(300))

    @staticmethod
    def add(url, text):
        stu = binance_notice_temp(url=url, text=text)
        session.add(stu)
        session.commit()

    @staticmethod
    def truncate():
        sql = """truncate table binance_notice_temp"""
        session.execute(sql)
        session.commit()


class binance_sitemap_en_9(DB):
    __tablename__ = 'binance_sitemap_en_9'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(TEXT)

    @staticmethod
    def add(url):
        stu = binance_sitemap_en_9(url=url)
        session.add(stu)
        session.commit()

    @staticmethod
    def truncate():
        sql = """truncate table binance_sitemap_en_9"""
        session.execute(sql)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(binance_sitemap_en_9).all():
            data.append(i.url)
        return data


def differ(table, temp_table):
    sql = 'select distinct url,text from {} where url  not in (select url from {});'.format(temp_table, table)
    ret = session.execute(sql)
    data = []
    for i in ret:
        data.append({
            "url": i.url,
            "text": i.text
        })
    return data


def copy_table(table, temp_table):
    sql = """insert into {} select * from {};""".format(table, temp_table)
    session.execute(sql)
    session.commit()


def binance():
    html = urlopen(url='https://www.binance.com/zh-CN/support/announcement')
    bs = BeautifulSoup(html.read(), 'html.parser')
    binance_notice_temp.truncate()  # 清空临时数据表
    data = []  # 存放差异数据list
    for i in bs.find_all(class_='css-qinc3w'):
        data.append({
            "url": "https://www.binance.com/" + i.attrs["href"],
            "title": i.get_text()
        })

    for i in data:
        # 数据写入临时数据表
        binance_notice_temp.add(i["url"], i["title"])

    dif = differ(temp_table="binance_notice_temp", table="binance_notice")  # 获得两张表比差数据
    if dif:
        binance_notice.truncate()  # 清空币安公告表
        copy_table("binance_notice", "binance_notice_temp")  # 复制临时表与公告表
        for i in data:
            send_message("币安交易所发布了新的公告:\n" +
                         "[{}]({})".format(i["title"], i["url"]))  # markdown格式传输文本
            time.sleep(1)
    else:
        pass


def binance_sitemap():
    html = urlopen(url="https://www.binance.com/sitemap_en_9.xml")
    bs = BeautifulSoup(html.read(), 'html.parser')
    data = []
    for i in bs.find_all("loc"):  # 获取url
        data.append(i.text)

    dif = list(set(data).difference(set(binance_sitemap_en_9.query())))   # 比差集
    if dif:
        for i in dif:
            binance_sitemap_en_9.add(i)
            send_message("""币安交易所sitemap9添加了新的页面:\n{}""".format(i))
            time.sleep(1)
    else:
        pass
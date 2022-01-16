from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.orm import sessionmaker
from config import databases

engine = create_engine(databases.DB_URI)
DB = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()


class binance_db(DB):
    __tablename__ = 'binance_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = binance_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(binance_db).all():
            data.append(i.coin)
        return data


class okex_db(DB):
    __tablename__ = 'okex_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = okex_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(okex_db).all():
            data.append(i.coin)
        return data


class coinbase_db(DB):
    __tablename__ = 'coinbase_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = coinbase_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(coinbase_db).all():
            data.append(i.coin)
        return data


class ftx_db(DB):
    __tablename__ = 'ftx_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = ftx_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(ftx_db).all():
            data.append(i.coin)
        return data


class gateio_db(DB):
    __tablename__ = 'gateio_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = gateio_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(gateio_db).all():
            data.append(i.coin)
        return data


class huobi_db(DB):
    __tablename__ = 'huobi_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = huobi_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(huobi_db).all():
            data.append(i.coin)
        return data


class kucoin_db(DB):
    __tablename__ = 'kucoin_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = kucoin_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(kucoin_db).all():
            data.append(i.coin)
        return data


class mexc_db(DB):
    __tablename__ = 'mexc_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = mexc_db(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(mexc_db).all():
            data.append(i.coin)
        return data

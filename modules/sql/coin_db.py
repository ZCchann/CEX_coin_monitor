from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.orm import sessionmaker
from config import databases

engine = create_engine(databases.DB_URI)
DB = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()


class binance(DB):
    __tablename__ = 'binance_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = binance(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(binance).all():
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


class coinbase(DB):
    __tablename__ = 'coinbase_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = coinbase(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(coinbase).all():
            data.append(i.coin)
        return data


class ftx(DB):
    __tablename__ = 'ftx_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = ftx(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(ftx).all():
            data.append(i.coin)
        return data


class gateio(DB):
    __tablename__ = 'gateio_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = gateio(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(gateio).all():
            data.append(i.coin)
        return data


class huobi(DB):
    __tablename__ = 'huobi_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = huobi(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(huobi).all():
            data.append(i.coin)
        return data


class kucoin(DB):
    __tablename__ = 'kucoin_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = kucoin(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(kucoin).all():
            data.append(i.coin)
        return data


class mexc(DB):
    __tablename__ = 'mexc_coin'  # 表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(VARCHAR(64))

    @staticmethod
    def add(coin):
        stu = mexc(coin=coin)
        session.add(stu)
        session.commit()

    @staticmethod
    def query():
        data = []
        for i in session.query(mexc).all():
            data.append(i.coin)
        return data

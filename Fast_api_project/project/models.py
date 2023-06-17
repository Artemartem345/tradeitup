from sqlalchemy import create_engine, Column, DateTime, String, Float, MetaData, Integer
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()
metadata = MetaData()

engine = create_engine('postgresql://localhost/crypto?user=artem&password=1234')
def connect_db():
    # engine = create_engine('postgresql://localhost/crypto?user=artem&password=1234')
    session = scoped_session(sessionmaker(bind=engine))
    return session




Base.metadata.create_all(engine)


class CryptoCourse(Base):  
    __tablename__ = 'cryptos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String)
    course = Column(Float)
    time = Column(DateTime)

# db = connect_db()
# btc = CryptoCourse(currency='BTC', course='26500.0', time=datetime.utcnow())
# db.add(btc)
# db.commit()


   
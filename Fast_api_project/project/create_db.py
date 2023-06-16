from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, DateTime, Integer
from sqlalchemy.orm import sessionmaker

def main():
    engine = create_engine('postgresql://localhost/crypto?user=artem&password=1234')
    Session = sessionmaker(bind=engine) 
    connection = engine.raw_connection()
    cursor = connection.cursor()
    session = Session()

    meta = MetaData()
    cryptos = Table(
        'cryptos', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('currency', String),
        Column('course', Float),
        Column('time', DateTime)
    )
    
   
#     meta.drop_all(bind=engine) 
#     meta.create_all(bind=engine)
    
# if __name__ == "__main__":
#     main()
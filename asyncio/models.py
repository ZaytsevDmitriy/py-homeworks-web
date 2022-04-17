import aiohttp
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://admin:1234@127.0.0.1:5432/asyncio_netology')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Person_model(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    birth_year = Column(Date)
    eye_color = Column(String(20))
    films = Column(String)
    gender = Column(String(20))
    hair_color = Column(String(20))
    height = Column(Integer)
    homeworld = Column(String)
    mass = Column(Integer)
    name = Column(String(100), nullable=False)
    skin_color = Column(String(20))
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)


    some_string = " ".join(flexiple))

async def get_info(url -> string:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_ENDPOINT}') as response:
            response = await response.json()
            return response


Base.metadata.create_all(engine)

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import func

engine = create_engine('postgresql://admin:1234@127.0.0.1:5432/flask_netology')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False, unique=True)

    email = Column(String)
    registration_time = Column(DateTime, server_default=func.now())
    password = Column(String, nullable=False)

    def to_dict(self):
        return {
            'user_name': self.user_name,
            'registration_time': int(self.registration_time.timestamp()),
            'id': self.id,
        }


class Ad(Base):
    __tablename__ = 'ad'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    stamp_time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))


Base.metadata.create_all(engine)